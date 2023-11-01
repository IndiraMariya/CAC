from itertools import combinations

import textacy
from textacy import extract
from keybert import KeyBERT
from keyphrase_vectorizers import KeyphraseCountVectorizer
import spacy

nlp = spacy.load("en_core_web_md")
key_bert = KeyBERT()
keyphrase_count_vectorizer = KeyphraseCountVectorizer()

SIMILARITY_THRESHOLD = 0.9

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


def extract_keybert_keyterms(data, kw_model=key_bert, vectorizer=keyphrase_count_vectorizer, only_keywords=True,
                             max_keys=5, debug=False):
    if not vectorizer:
        keywords = kw_model.extract_keywords(data, keyphrase_ngram_range=(1, 3), stop_words="english")
    else:
        keywords = kw_model.extract_keywords(data, vectorizer=vectorizer, use_mmr=True, diversity=0.5)

    if debug:
        print(keywords)

    if only_keywords:
        return [[tag for (tag, num) in article_kw][:max_keys] for article_kw in keywords]

    return keywords


# def remove_similar_terms(terms: list[list[str]], _nlp=nlp):
#     # based on: https://towardsdatascience.com/how-to-filter-out-similar-texts-in-python-c7e7c5f7620e
#     embeddings = [[_nlp(term) for term in term_group] for term_group in terms]

#     for embeddings_group in embeddings:
#         all_pairs = list(combinations(embeddings_group, 2))

#         similar_terms = [(p1, p2) for p1, p2 in all_pairs if p1.similarity(p2) > SIMILARITY_THRESHOLD]

#     # TODO: combine similar terms to a singular term

#     pass

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
