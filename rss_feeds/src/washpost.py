#!/usr/bin/python3 
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
from supabase import Client
import os
import re

count = 0     

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

        for a in self.articles:
            title = a.find('title').text if a.find('title') else ''
            link = a.find('link').text if a.find('link') else ''
            description = a.find('description').text if a.find('description') else ''
            pubdate = a.find('pubDate').text if a.find('pubDate') else ''
            article_data = {
                'title': title,
                'href': link,
                'description': description,
                'author': "",
                'date': pubdate,
                'src': find_image(link),
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
    if data.data and data.data[0].get('status') == 'ok':
        count = count + 1


def find_image(article_url):
    try:
        # Send a GET request to the article URL
        response = requests.get(article_url)
        response.raise_for_status()  # Raise an exception for any HTTP errors
        # Parse the HTML content of the article
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the image element by inspecting the HTML structure of the webpage
        img_element = soup.find('img', {'style': re.compile(r'background-image:.*url\([\'"](.*?)[\'"]\)')})

        if img_element:
            # Extract the image URL from the 'srcset' attribute
            srcset_attr = img_element.get('srcset')
            if srcset_attr:
                # Split the srcset attribute by commas to separate different URLs
                image_urls = [url.strip() for url in srcset_attr.split(',')]
                # Take the first URL as the top image (you can adjust this logic)
                top_image_url = image_urls[0].split()[0]
                # Display the top image URL
                return(top_image_url)
            else:
                print("No 'srcset' attribute found for the image.")
        else:
            print("No image found on the webpage.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the article: {e}")

