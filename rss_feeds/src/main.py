# from washpost import washpost
# import os
# from dotenv import load_dotenv
# from supabase import Client
# import csv
# # import clean_data
# from washpost import ReadRss
from clean_data import clearArticles
from washpost import ReadWashpost
from nyt import ReadNYT
from fox import ReadFox
import os
from dotenv import load_dotenv
from supabase import Client
import csv


headers = {
    'User-Agent': 'your-user-agent-here'
}
load_dotenv()


if __name__ == '__main__':
    clearArticles()

    def switch_source(case):
        if case == 'Washington Post':
            ReadWashpost(row[0], headers, row[1])
            print(f"{case} articles successfully added" )
        elif case == 'New York Times':
            ReadNYT(row[0], headers, row[1])
            print(f"{case} articles successfully added" )
        elif case == 'Fox News':
            ReadFox(row[0], headers, row[1])
            print(f"{case} articles successfully added" )
        elif case == 'Wall Street Journal':
            print("This is case 4")
        else:
            print("This is the default case")

    path = os.environ.get('SOURCE_PATH')
    
    with open (path) as file:
        content = csv.reader(file)
        for row in content:
            source = row[1]
            switch_source(source)
