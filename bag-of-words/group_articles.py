import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.cluster import HDBSCAN

from sklearn.decomposition import TruncatedSVD
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Normalizer

from nltk.stem.snowball import SnowballStemmer

import string
import json

from keyword_extraction import extract_keybert_keyterms
from subjectivity_analysis import get_subjectivities
from utilities import get_supabase_client, read_data_from_supabase, get_grouped_data

supabase = get_supabase_client()

# load in data
print("Reading in data")
response = read_data_from_supabase(supabase)
data = [[article['id'], article['articleData']['title'], article['articleData']['description']] for article in response.data if article is not None and article["articleData"] is not None]
data = pd.DataFrame(data, columns=["id", "title", "description"])

print("Data read from supabase")
# deal with missing data
data = data.fillna("")

# combine text fields
combined = pd.DataFrame(data["title"] + "; " + data["description"], columns=["text"])
combined['id'] = data['id']

# Stemming
print("Performing Stemming")
stemmer = SnowballStemmer("english", ignore_stopwords=True)
combined['stemmed'] = combined['text'].apply(
    lambda x:
        ' '.join([
            stemmer.stem(word) for word in x.translate(
                str.maketrans('', '', string.punctuation) # remove punctuation
            ).split(' ')
        ])
)

# create bag of words
count_vect = CountVectorizer(
    stop_words="english",
    # ngram_range=(1,2) # count words and pairs of words
)
X_train_counts = count_vect.fit_transform(combined['stemmed'])
print("Bag of Words created!")

# tfidf = Term Frequency times Inverse Document Frequency
# removes weighting based on text document length
tfidf_transformer = TfidfTransformer()
X_tfidf = tfidf_transformer.fit_transform(X_train_counts)
print("TFIDF complete")

# perform lsa (reduce size of dataset)
lsa = make_pipeline(TruncatedSVD(n_components=100), Normalizer(copy=False))
X_lsa = lsa.fit_transform(X_tfidf)
explained_variance = lsa[0].explained_variance_ratio_.sum()
print(f"Explained variance of the SVD step: {explained_variance * 100:.1f}%")

# grouping algorithms
K_MEANS = 0
AGGLO = 1
_DBSCAN = 2

ALG = AGGLO

print("Clustering...")
if ALG == K_MEANS:
    NUM_CLUSTERS = 60
    # cluster (k-means)
    clusterer = KMeans(
        n_clusters=NUM_CLUSTERS,
        max_iter=100,
        n_init=1,

    ).fit(X_lsa)
    cluster_ids, cluster_sizes = np.unique(clusterer.labels_, return_counts=True)
    print(f"Number of elements assigned to each cluster: {cluster_sizes}")

    # get top words in each cluster (k-means only)
    original_space_centroids = lsa[0].inverse_transform(clusterer.cluster_centers_)
    order_centroids = original_space_centroids.argsort()[:, ::-1]
    terms = count_vect.get_feature_names_out()

    for i in range(NUM_CLUSTERS):
        print(f"Cluster {i}: ", end="")
        for ind in order_centroids[i, :10]:
            print(f"{terms[ind]} ", end="")
        print()
elif ALG == AGGLO:
    # cluster (agglomerative / hierarchical)
    clusterer = AgglomerativeClustering(
        n_clusters=None,
        metric="cosine",
        linkage='average',
        distance_threshold=0.75
    ).fit(X_lsa)
    cluster_ids, cluster_sizes = np.unique(clusterer.labels_, return_counts=True)
    NUM_CLUSTERS = len(cluster_sizes)
    print(f"Number of elements assigned to each cluster: {cluster_sizes}")
elif ALG == _DBSCAN:
    # cluster (DBSCAN)
    clusterer = DBSCAN(
        eps=0.6,
        metric='cosine'
    ).fit(X_lsa)
    cluster_ids, cluster_sizes = np.unique(clusterer.labels_, return_counts=True)
    NUM_CLUSTERS = len(cluster_sizes)
    print(f"Number of elements assigned to each cluster: {cluster_sizes}")

data['topic'] = clusterer.labels_
combined['topic'] = clusterer.labels_

# for cluster in range(NUM_CLUSTERS):
#     print("-------------- CLUSTER #" + str(cluster))
#     print(data.loc[data['topic'] == cluster]['title'])

# get tags
print("analyzing topics")
grouped_data_as_list = get_grouped_data(combined)
tags = extract_keybert_keyterms(grouped_data_as_list)
data['tags'] = data['topic'].map({topic: tags for topic, tags in enumerate(tags)})

# get subjectivity
print("analyzing subjectivity")
subjectivities = get_subjectivities(combined['text'].values.tolist())
data['bias'] = subjectivities

# write data to supabase
only_topics_df = data[['id', 'title', 'topic', 'tags', 'bias']]
only_topics_df = only_topics_df.rename(columns={'title': "name"})

print(only_topics_df.head())

# convert to json
json_str = only_topics_df.to_json(orient="records")
json_data = json.loads(json_str)

# update supabase
print("writing to supabase")
val = supabase.table('Data').upsert(json_data).execute()
print("writing complete!")
