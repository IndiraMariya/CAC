# from washpost import washpost
# import os
# from dotenv import load_dotenv
# from supabase import Client
# import csv
# # import clean_data
# from washpost import ReadRss
from washpost import ReadRss
import os
from dotenv import load_dotenv
from supabase import Client
import csv


headers = {
    'User-Agent': 'your-user-agent-here'
}



if __name__ == '__main__':
    def switch_source(case):
        if case == 'Washington Post':
            ReadRss(row[0], headers, row[1])
            print(f"{case} successfully added" )
        elif case == 'New York Times':
            print("This is case 2")
        elif case == 'Fox News':
            print("This is case 3")
        elif case == 'Wall Street Journal':
            print("This is case 4")
        else:
            print("This is the default case")

    path = os.environ.get('SOURCE_PATH')
    
    with open ('/Users/indiram/Work/CAC/rss_feeds/rss_feeds.csv') as file:
        content = csv.reader(file)
        for row in content:
            source = row[1]
            switch_source(source)
    
    # print(f"{count} Articles Added")
    # clean_data.clearArticles()
