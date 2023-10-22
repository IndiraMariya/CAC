#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import feedparser
from dateutil.parser import parse
import datetime
from supabase import Client

headers = {
    'User-Agent': 'your-user-agent-here'
}
load_dotenv()
count = 0

class ReadWSJ:
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
        
        articleIndex = 0  # Initialize article index
        feed = feedparser.parse(rss_url)
        count = len(feed.entries)

        for a in self.articles:
            title = a.find('title').text if a.find('title') else ''
            link = feed.entries[articleIndex].link
            description = a.find('description').text if a.find('description') else ''
            pubdate = a.find('pubDate').text if a.find('pubDate') else ''
            image_url = fetchImg(link)

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
        "date":date}).execute()
    assert len(data.data) > 0
    count = count + 1

def fetchImg(link):
    url = link
    response = requests.get(url)
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')

        if len(img_tags) >= 2:
            # Get the second image's 'src' attribute
            second_image_url = img_tags[1]['src']
            print("Second Image URL:", second_image_url)
            return second_image_url
        else:
            print("There are not enough images on the page to retrieve the second one.")
            return ""
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return ""
        

if __name__ == '__main__':
    ReadWSJ("https://feeds.a.dj.com/rss/WSJcomUSBusiness.xml", headers, "Wall Street Journal")