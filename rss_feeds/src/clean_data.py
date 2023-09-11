from dotenv import load_dotenv
import os
from supabase import Client
from datetime import datetime, timedelta
from dateutil import parser
import pytz

def clearArticles():
    load_dotenv()
    url = os.environ.get('SUPABASE_URL')
    api_key = os.environ.get('SUPABASE_KEY')

    # Initialize the Supabase client
    supabase = Client(url, api_key)

    # Fetch data based on deletion criteria
    response = supabase.table('Data').select("*").execute()
    data_to_delete = response.data

    tzinfos = {"EDT": pytz.timezone("US/Eastern")}
    count = 0

    # Print JSON dates from the "date" key within "articleData" field
    for row in data_to_delete:
        if "articleData" in row and "date" in row["articleData"]:
            json_date = row["articleData"]["date"]
            # Parse the JSON date using dateutil.parser with timezone mapping
            json_datetime = parser.parse(json_date, tzinfos=tzinfos)
            one_month_ago = datetime.now(pytz.timezone('US/Eastern')) - timedelta(days=20)
            
            # Check if the JSON date is older than one month ago in Pacific timezone
            if json_datetime < one_month_ago:
                delete_response = supabase.table("Data").delete().eq("id", row["id"]).execute()
                # print(f"Deleted row with ID {row['id']}")
                count = count+1
        
    print(f"{count} Articles Deleted")