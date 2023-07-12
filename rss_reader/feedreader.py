from bs4 import BeautifulSoup
import requests
import json

headers = {
    'User-Agent': 'your-user-agent-here'
}
 
class ReadRss:
    def __init__(self, rss_url, headers):
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
                'newsSource': ""
            })
        self.urls = [d['link'] for d in self.articles_dicts if 'link' in d]
        self.titles = [d['title'] for d in self.articles_dicts if 'title' in d]
        self.descriptions = [d['description'] for d in self.articles_dicts if 'description' in d]
        self.pub_dates = [d['pubdate'] for d in self.articles_dicts if 'pubdate' in d]
 
if __name__ == '__main__':
    feed = ReadRss('https://feeds.washingtonpost.com/rss/politics', headers)
    
    with open('articles.json', 'w') as file:
        for article in feed.articles_dicts:
            json_str = json.dumps(article, indent=4)
            file.write(json_str)
            file.write('\n')
    
