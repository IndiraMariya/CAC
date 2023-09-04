import washpost
from . import os
from supabase import Client

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

if __name__ == '__main__':
    path = os.environ.get('SOURCE_PATH')
    with open (path) as file:
        content = csv.reader(file)
        for row in content:
            feed = washpost.ReadRss(row[0], headers, row[1])
    print(f"{count} Articles Added")
