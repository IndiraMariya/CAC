from supabase import create_client, Client
from dotenv import load_dotenv
import os


def getSupabaseClient() -> Client:
    load_dotenv()
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    print("establishing client")
    supabase: Client = create_client(url, key)

    return supabase


