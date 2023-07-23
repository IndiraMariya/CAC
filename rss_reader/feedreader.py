from bs4 import BeautifulSoup
import requests
import json
import csv

headers = {
    'User-Agent': 'your-user-agent-here'
}

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
            self.articles_dicts.append({
                'title': title,
                'href': link,
                'description': description,
                'author': "",
                'date': pubdate,
                'src': "https://images-fibreglast-com.s3.amazonaws.com/pio-resized/750/Single%20Stage%20Light%20Blue%20Paint-24.jpg",
                'alt': "",
                'newsSource': source
            })
        self.urls = [d['href'] for d in self.articles_dicts]
        self.titles = [d['title'] for d in self.articles_dicts]
        self.descriptions = [d['description'] for d in self.articles_dicts]
        self.pub_dates = [d['date'] for d in self.articles_dicts]

# if __name__ == '__main__':
with open ('rss_feeds.csv') as file:
    content = csv.reader(file)
    for row in content:
        feed = ReadRss(row[0], headers, row[1])
        with open('articles.json', 'a') as file:
            json.dump(feed.articles_dicts, file, indent=4)
