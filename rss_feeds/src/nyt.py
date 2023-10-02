#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import csv
from dotenv import load_dotenv
import os
from supabase import Client
import json
import re 

headers = {
    'User-Agent': 'your-user-agent-here'
}
load_dotenv()

count = 0
articleIndex = 0      

class ReadNYT:
    def __init__(self, rss_url, headers, source):
        global articleIndex
        self.url = rss_url
        self.headers = headers
        try:
            self.r = requests.get(rss_url, headers=self.headers)
            self.status_code = self.r.status_code
        except Exception as e:
            print('Error fetching the URL:', rss_url)
            print(e)
        try:
            self.soup = BeautifulSoup(self.r.text, 'xml')
        except Exception as e:
            print('Could not parse the XML:', self.url)
            print(e)
        self.articles = self.soup.findAll('item')
        self.articles_dicts = []
        find_image(rss_url)

        for a in self.articles:
            title = a.find('title').text if a.find('title') else ''
            link = a.find('link').text if a.find('link') else ''
            description = a.find('description').text if a.find('description') else ''
            pubdate = a.find('pubDate').text if a.find('pubDate') else ''

            # Check if articleIndex is within bounds
            if articleIndex < len(image_data):
                article_data = {
                    'title': title,
                    'href': link,
                    'description': description,
                    'author': "",
                    'date': pubdate,
                    'src': image_data[articleIndex],
                    'alt': "",
                    'newsSource': source
                }
                self.articles_dicts.append(article_data)  # Append the dictionary
                add_data(article_data)  # Run the add data method to send data to supabase
                articleIndex += 1
            else:
                article_data = {
                    'title': title,
                    'href': link,
                    'description': description,
                    'author': "",
                    'date': pubdate,
                    'src': "data:image/png;base64,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",
                    'alt': "",
                    'newsSource': source
                }
                self.articles_dicts.append(article_data)  # Append the dictionary
                add_data(article_data)  # Run the add data method to send data to supabase
                articleIndex += 1

        self.urls = [d['href'] for d in self.articles_dicts]
        self.titles = [d['title'] for d in self.articles_dicts]
        self.descriptions = [d['description'] for d in self.articles_dicts]
        self.pub_dates = [d['date'] for d in self.articles_dicts]


def add_data(article_data):
    global count
    url = os.environ.get('SUPABASE_URL')
    api_key = os.environ.get('SUPABASE_KEY')
    # Initialize the Supabase client
    supabase = Client(url, api_key)

    name = article_data['title']
    newsSource = article_data['newsSource']
    #insert data
    data = supabase.table("Data").upsert({
        "name":name, 
        "articleData": article_data, 
        "newsSource": newsSource}).execute()
    assert len(data.data) > 0
    count = count + 1
        

def find_image(rss_link):
    global image_data
    image_data = []
    try:
        # Send a GET request to the RSS feed URL
        response = requests.get(rss_link)
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the XML content of the RSS feed
            soup = BeautifulSoup(response.content, 'xml')
            # Find all <item> elements in the RSS feed
            items = soup.find_all('item')
            # Iterate through <item> elements
            for item in items:
                # Extract the image URL from <media:content> tag
                media_content = item.find('media:content', {"medium": "image"})
                if media_content:
                    image_url = media_content['url']
                    image_data.append(image_url)  # Append image URL to image_data list
                else:
                    # If no image URL is found, append an empty string to image_data
                    image_data.append('')
        else:
            print(f"Failed to fetch Images. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# if __name__ == '__main__':
path = os.environ.get('SOURCE_PATH')
with open (path) as file:
    content = csv.reader(file)
    for row in content:
        feed = ReadRss(row[0], headers, row[1])
print(f"{count} Articles Added")
