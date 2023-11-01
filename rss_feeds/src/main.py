from clean_data import clearArticles
from washpost import ReadWashpost
from nyt import ReadNYT
from fox import ReadFox
import os
from dotenv import load_dotenv
from supabase import Client
import csv

# from topic.group_articles import groupArticles
from topic.utilities import get_supabase_client, read_data_from_supabase, get_grouped_data

headers = {
    'User-Agent': 'your-user-agent-here'
}
load_dotenv()


if __name__ == '__main__':
    clearArticles()

    def switch_source(case):
        if case == 'Washington Post':
            ReadWashpost(row[0], headers, row[1], row[2])
            print(f"{case} articles successfully added" )
        elif case == 'New York Times':
            ReadNYT(row[0], headers, row[1], row[2])
            print(f"{case} articles successfully added" )
        elif case == 'Fox News':
            ReadFox(row[0], headers, row[1], row[2])
            print(f"{case} articles successfully added" )
        elif case == 'Vox':
            print("This is Vox")
        elif case == 'CNN':
            print("This is CNN")
        elif case == 'New York Post':
            print("This is NYP")
        elif case == 'Daily Mail':
            print("This is DM")
        else:
            print("This is the default case")

    path = os.environ.get('SOURCE_PATH')
    
    with open (path) as file:
        content = csv.reader(file)
        for row in content:
            source = row[1]
            switch_source(source)
    # groupArticles()
