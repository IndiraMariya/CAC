from clean_data import clearArticles
from washpost import ReadWashpost
from article_update import ReadRss
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
            ReadRss(row[0], headers, row[1], row[2])
        elif case == 'CNN':
            ReadRss(row[0], headers, row[1], row[2])
        elif case == 'New York Post':
            ReadRss(row[0], headers, row[1], row[2])
        else:
            print("This is the default case")

    path = os.environ.get('SOURCE_PATH')
    
    with open (path) as file:
        content = csv.reader(file)
        for row in content:
            source = row[1]
            switch_source(source)
    # groupArticles()
