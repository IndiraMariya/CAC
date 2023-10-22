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

class ReadRss:
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
                    'src': "",
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
