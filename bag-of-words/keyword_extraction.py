import textacy
from textacy import extract

from utilities import read_data_from_csv, combine_text_fields

df = read_data_from_csv()
filled_data = df.fillna("")
combined = combine_text_fields(filled_data, other_fields=["id", "topic"])

grouped_data = combined.groupby('topic', as_index=False).agg({"text": ' '.join})

list_data = grouped_data["text"].values.tolist()

test_data = list_data[0]

doc = textacy.make_spacy_doc(test_data, lang="en_core_web_sm")

POS = ['PROPN', 'NOUN', 'ADJ', 'VERB', 'ADV']
TOP_N = 10
NORMALIZER = textacy.spacier.utils.get_normalized_text

print(extract.keyterms.textrank(doc, normalize=NORMALIZER, include_pos=POS, topn=TOP_N))
print(extract.keyterms.yake(doc, normalize='lemma', include_pos=POS, topn=TOP_N))
print(extract.keyterms.scake(doc, normalize=NORMALIZER, include_pos=POS, topn=TOP_N))
print(extract.keyterms.sgrank(doc, ngrams=(1, 2, 3), normalize=NORMALIZER, include_pos=POS, topn=TOP_N))

