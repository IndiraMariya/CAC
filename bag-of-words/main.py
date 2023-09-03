# Based on: https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

DATA_FP = "datasets/MINDlarge_train/news.tsv"

data = pd.read_csv(DATA_FP, sep='\t')
data.columns = ['id', 'category', 'subcategory', 'title', 'abstract', 'url', 'title entities', 'abstract entities']

data = data.fillna("")

combined = pd.DataFrame(data["title"] + ";" + data["abstract"], columns=["text"])

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(combined['text'])
print(X_train_counts.shape)

print(count_vect.vocabulary_.get(u'president'))
