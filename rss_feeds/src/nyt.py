#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
from dateutil.parser import parse
import datetime
from supabase import Client


headers = {
    'User-Agent': 'your-user-agent-here'
}
count = 0
load_dotenv()

sourceLean = ""

class ReadNYT:
    def __init__(self, rss_url, headers, source, lean):
        global articleIndex
        self.url = rss_url
        self.headers = headers
        sourceLean = lean
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
        # find_image(rss_url)

        for a in self.articles:
            title = a.find('title').text if a.find('title') else ''
            link = a.find('link').text if a.find('link') else ''
            description = a.find('description').text if a.find('description') else ''
            pubdate = a.find('pubDate').text if a.find('pubDate') else ''
            image_url = fetch_image_url(self, a)

            article_data = {
                'title': title,
                'href': link,
                'description': description,
                'author': "",
                'date': pubdate,
                'src': image_url,
                'alt': "",
                'newsSource': source
            }
            self.articles_dicts.append(article_data)  # Append the dictionary
            add_data(article_data)  # Run the add data method to send data to supabase

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

    article_date = parse(article_data['date'], fuzzy=True)
    date = article_date.strftime("%m/%d/%Y, %H:%M:%S")
    #insert data
    data = supabase.table("Data").upsert({
        "name":name, 
        "articleData": article_data, 
        "newsSource": newsSource,
        "date":date,
        "source_lean": sourceLean,}).execute()
    assert len(data.data) > 0
    count = count + 1
    
def fetch_image_url(self, article):
    media_content = article.find('media:content', {"medium": "image"})
    if media_content:
        return media_content['url']
    else:
        return ''
        


if __name__ == '__main__':
    ReadNYT("https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml", headers, "New York Times", "Far Left")