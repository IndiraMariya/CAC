from dotenv import load_dotenv
import os
from supabase import Client
import json


load_dotenv()
url = os.environ.get('SUPABASE_URL')
api_key = os.environ.get('SUPABASE_KEY')
# Initialize the Supabase client
supabase = Client(url, api_key)


# Iterate through each element in the JSON data
for article in data:
    # Extract the title
    name = article['title']
    newsSource = article['newsSource']
    #insert data
    data = supabase.table("Data").upsert({
        "name":name, 
        "articleData": article, 
        "newsSource": newsSource}).execute()
    assert len(data.data) > 0

    



