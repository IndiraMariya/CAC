import os
from dotenv import load_dotenv
from supabase import create_client, Client
import pandas as pd

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# load in data
response = supabase.table('Data').select("*").execute()
data = [[article['id'], article['articleData']['title'], article['articleData']['description']] for article in response.data]
df = pd.DataFrame(data, columns=["id", "title", "description"])