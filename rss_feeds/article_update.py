#!/usr/bin/python3 
from bs4 import BeautifulSoup
import requests
import csv
from dotenv import load_dotenv
import os
from supabase import Client
import json

headers = {
    'User-Agent': 'your-user-agent-here'
}
load_dotenv()
class ReadRss:
    def __init__(self, rss_url, headers, source):
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
                'src': "https://images-fibreglast-com.s3.amazonaws.com/pio-resized/750/Single%20Stage%20Light%20Blue%20Paint-24.jpg",
                'alt': "",
                'newsSource': source
            }
            self.articles_dicts.append(article_data)  # Append the dictionary
            add_data(article_data) #run the add data method to send data to supabase

        self.urls = [d['href'] for d in self.articles_dicts]
        self.titles = [d['title'] for d in self.articles_dicts]
        self.descriptions = [d['description'] for d in self.articles_dicts]
        self.pub_dates = [d['date'] for d in self.articles_dicts]
        


def add_data(article_data):
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


# if __name__ == '__main__':
path = os.environ.get('SOURCE_PATH')
with open (path) as file:
    print("Articles Added")
    content = csv.reader(file)
    for row in content:
        feed = ReadRss(row[0], headers, row[1])
