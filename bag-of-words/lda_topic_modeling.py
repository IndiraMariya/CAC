import spacy
from gensim.utils import simple_preprocess
from gensim.models import Phrases, LdaModel, CoherenceModel
from gensim.models.phrases import Phraser
import gensim.corpora as corpora
from nltk.corpus import stopwords

from utilities import read_data_from_csv, combine_text_fields


def sent_to_words(sentences):
    for sentence in sentences:
        yield simple_preprocess(str(sentence), deacc=True)  # deacc=True removes punctuations


# =================================== Read in data
df = read_data_from_csv('datasets/supabase_data/data.csv')
combined = combine_text_fields(df)

data = combined['text'].values.tolist()
print(data[:1])

data_words = list(sent_to_words(data))
print(data_words[:1])

# =================================== Cleaning Data Utilities
# nltk stopwords
stop_words = stopwords.words('english')

# Build the bigram and trigram models
bigram = Phrases(data_words, min_count=5, threshold=100)  # higher threshold fewer phrases.
trigram = Phrases(bigram[data_words], threshold=100)

# Faster way to get a sentence clubbed as a trigram/bigram
bigram_mod = Phraser(bigram)
trigram_mod = Phraser(trigram)

# NLP model (only tagger)
nlp = spacy.load('en_core_web_lg')


def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]


def make_bigrams(texts):
    return [bigram_mod[doc] for doc in texts]


def make_trigrams(texts):
    return [trigram_mod[bigram_mod[doc]] for doc in texts]


def lemmatization(texts, allowed_postags=['PROPN', 'NOUN', 'ADJ', 'VERB', 'ADV']):
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent))
        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out


# =================================== Clean Data
# Remove Stop Words
data_words_nostops = remove_stopwords(data_words)

# Form Bigrams
data_words_bigrams = make_bigrams(data_words_nostops)

# Do lemmatization keeping only propernouns, noun, adjective, verb, adverb
data_lemmatized = lemmatization(data_words_bigrams, allowed_postags=['PROPN', 'NOUN', 'ADJ', 'VERB', 'ADV'])

print(data_lemmatized[:1])

# =================================== Create Dictionary + Corpus
# Create Dictionary
id2word = corpora.Dictionary(data_lemmatized)

# Create Corpus
texts = data_lemmatized

# Term Document Frequency
corpus = [id2word.doc2bow(text) for text in texts]

# View
print([[(id2word[id], freq) for id, freq in cp] for cp in corpus[:1]])

# =================================== Build LDA Model
lda_model = LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=50,
                                           random_state=100,
                                           update_every=1,
                                           chunksize=10,
                                           passes=10,
                                           alpha='auto',
                                           per_word_topics=True)

# View topics
# Print the Keyword in the topics
print(lda_model.print_topics())
doc_lda = lda_model[corpus]

# Compute Perplexity
print('\nPerplexity: ', lda_model.log_perplexity(corpus))  # a measure of how good the model is. lower the better.

# Compute Coherence Score
coherence_model_lda = CoherenceModel(model=lda_model, texts=data_lemmatized, dictionary=id2word, coherence='c_v')
coherence_lda = coherence_model_lda.get_coherence()
print('\nCoherence Score: ', coherence_lda)
