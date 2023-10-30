from pandas import DataFrame

from textblob import TextBlob
from textblob.en.sentiments import NaiveBayesAnalyzer
from utilities import read_data_from_csv, combine_text_fields, get_grouped_data


# =============================== Read in Data
df = read_data_from_csv()
filled_data = df.fillna("")
combined: DataFrame = combine_text_fields(filled_data, other_fields=["id", "topic"])

list_data = get_grouped_data(combined)
test_data = list_data[0]
# test_data = list_data[:10]


# test blob
blob_words = combined["text"].values.tolist()


for word in blob_words[:10]:
    blob = TextBlob(word)
    blob2 = TextBlob(word, analyzer=NaiveBayesAnalyzer())

    print(word)
    print(blob.sentiment)
    print(blob.sentiment_assessments)
    print(blob2.sentiment)
