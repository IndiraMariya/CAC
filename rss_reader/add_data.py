from dotenv import load_dotenv
import os
from supabase import Client
import json


load_dotenv()
url = os.environ.get('SUPABASE_URL')
api_key = os.environ.get('SUPABASE_KEY')
# Initialize the Supabase client
supabase = Client(url, api_key)

idVal = 1

# Open the JSON file
with open('./articles.json') as f:
    data = json.load(f)

# Iterate through each element in the JSON data
for article in data:
    # Extract the title
    name = article['title']
    #insert data
    data = supabase.table("Data").insert({"id": idVal, "name":name, "articleData": article}).execute()
    assert len(data.data) > 0
    # Update the idVal index
    idVal += 1

    



