from pandas import DataFrame
from postgrest import APIResponse
from supabase import create_client, Client
from dotenv import load_dotenv
import os
import pandas as pd


def get_supabase_client() -> Client:
    load_dotenv()
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    print("establishing client")
    supabase: Client = create_client(url, key)

    return supabase


def read_data_from_supabase(client: Client, query="*", table='Data'):
    response = client.table(table).select(query).execute()
    return response


def save_data_to_csv(response: APIResponse, file_name='datasets/supabase_data/data.csv'):
    data = [[article['id'], article['articleData']['title'], article['articleData']['description'], article['topic']]
            for article in
            response.data]
    df = pd.DataFrame(data, columns=["id", "title", "description", "topic"])
    df.to_csv(file_name, index=False)

    print("Data successfully saved!")


def read_data_from_csv(file_name='datasets/supabase_data/data.csv') -> DataFrame:
    data = pd.read_csv(file_name)
    return data

def combine_text_fields(df: DataFrame, field_1="title", field_2="description", combined_name="text", other_fields=['id']) -> DataFrame:
    # combine text fields
    combined = pd.DataFrame(df[field_1] + "; " + df[field_2], columns=[combined_name])

    for field in other_fields:
        combined[field] = df[field]
    return combined

def get_grouped_data(combined_data) -> list:
    grouped_data = combined_data.groupby('topic', as_index=False).agg({"text": ' '.join})
    # print(grouped_data.iloc[0])

    # convert topics to integers
    grouped_data['topic'] = pd.to_numeric(grouped_data['topic'], downcast='integer')

    # sort data by topic
    sorted_data = grouped_data.sort_values(by='topic')
    # print(sorted_data['text'].iloc[0])

    # convert to list
    list_data = sorted_data["text"].values.tolist()
    return list_data