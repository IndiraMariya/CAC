import textacy
from textacy import extract
from keybert import KeyBERT
from keyphrase_vectorizers import KeyphraseCountVectorizer

# =============================== Key Term Functions
def extract_texacy_keyterms(data):
    doc = textacy.make_spacy_doc(data, lang="en_core_web_sm")

    POS = ['PROPN', 'NOUN', 'ADJ', 'VERB', 'ADV']
    TOP_N = 10
    NORMALIZER = textacy.spacier.utils.get_normalized_text

    textrank = extract.keyterms.textrank(doc, normalize=NORMALIZER, include_pos=POS, topn=TOP_N)
    yake = extract.keyterms.yake(doc, normalize='lemma', include_pos=POS, topn=TOP_N)
    scake = extract.keyterms.scake(doc, normalize=NORMALIZER, include_pos=POS, topn=TOP_N)
    sgrank = extract.keyterms.sgrank(doc, ngrams=(1, 2, 3), normalize=NORMALIZER, include_pos=POS, topn=TOP_N)

    print(textrank)
    print(yake)
    print(scake)
    print(sgrank)

    return textrank, yake, scake, sgrank


def extract_keybert_keyterms(data, kw_model=KeyBERT(), vectorizer=KeyphraseCountVectorizer(), only_keywords=True, debug=False):
    if not vectorizer:
        keywords = kw_model.extract_keywords(data, keyphrase_ngram_range=(1, 3), stop_words="english")
    else:
        keywords = kw_model.extract_keywords(data, vectorizer=vectorizer)
    if debug: print(keywords)

    if only_keywords: return [[tag for (tag, num) in article_kw] for article_kw in keywords]

    return keywords


# Create KeyBERT
# kw_model = KeyBERT()
# nlp = spacy.load("en_core_web_lg", exclude=['tagger', 'parser', 'ner', 'attribute_ruler', 'lemmatizer'])
# kw_spacy_model = KeyBERT(model=nlp)
# vectorizer = KeyphraseCountVectorizer()

# print("---- TEXACY KEYTERMS ----")
# extract_texacy_keyterms()

# print("---- KeyBERT KEYTERMS ----")
# extract_keybert_keyterms(test_data, kw_model, vectorizer=None)
# extract_keybert_keyterms(test_data, kw_spacy_model, vectorizer=None)
# extract_keybert_keyterms(test_data, kw_model, debug=True)  # best atm
# extract_keybert_keyterms(test_data, kw_spacy_model)
