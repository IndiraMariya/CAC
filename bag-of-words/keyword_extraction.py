import textacy
import spacy
from textacy import extract
from keybert import KeyBERT
from keyphrase_vectorizers import KeyphraseCountVectorizer

from utilities import read_data_from_csv, combine_text_fields

# =============================== Read in Data
df = read_data_from_csv()
filled_data = df.fillna("")
combined = combine_text_fields(filled_data, other_fields=["id", "topic"])
grouped_data = combined.groupby('topic', as_index=False).agg({"text": ' '.join})
list_data = grouped_data["text"].values.tolist()

test_data = list_data[0]


# =============================== Create Spacy Doc
def extract_texacy_keyterms():
    doc = textacy.make_spacy_doc(test_data, lang="en_core_web_sm")

    POS = ['PROPN', 'NOUN', 'ADJ', 'VERB', 'ADV']
    TOP_N = 10
    NORMALIZER = textacy.spacier.utils.get_normalized_text

    print(extract.keyterms.textrank(doc, normalize=NORMALIZER, include_pos=POS, topn=TOP_N))
    print(extract.keyterms.yake(doc, normalize='lemma', include_pos=POS, topn=TOP_N))
    print(extract.keyterms.scake(doc, normalize=NORMALIZER, include_pos=POS, topn=TOP_N))
    print(extract.keyterms.sgrank(doc, ngrams=(1, 2, 3), normalize=NORMALIZER, include_pos=POS, topn=TOP_N))


def extract_keybert_keyterms(kw_model):
    keywords = kw_model.extract_keywords(test_data, keyphrase_ngram_range=(1, 3), stop_words="english")
    print(keywords)

# Create KeyBERT
kw_model = KeyBERT()
nlp = spacy.load("en_core_web_lg", exclude=['tagger', 'parser', 'ner', 'attribute_ruler', 'lemmatizer'])
kw_spacy_model = KeyBERT(model=nlp)

# print("---- TEXACY KEYTERMS ----")
# extract_texacy_keyterms()

print("---- KeyBERT KEYTERMS ----")
extract_keybert_keyterms(kw_model)
extract_keybert_keyterms(kw_spacy_model)
print(kw_model.extract_keywords(test_data, vectorizer=KeyphraseCountVectorizer()))
print(kw_spacy_model.extract_keywords(test_data, vectorizer=KeyphraseCountVectorizer()))
