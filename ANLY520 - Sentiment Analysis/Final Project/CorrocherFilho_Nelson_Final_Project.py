import random
import nltk
import codecs
import os
from bs4 import BeautifulSoup
from nltk.corpus import brown, stopwords
from nltk.tokenize import RegexpTokenizer
from timeit import default_timer as timer

# Common portion
htmlsource = 'C:\\Users\\corrocherfilhonw\\workspace\\polarity\\movie'
corpusdir = 'C:\\Users\\corrocherfilhonw\\workspace\\polarity\\corpus'

# code to convert the html to txt. Run only once.
#for filename in os.listdir(htmlsource):
#    print(filename)
#    fn = filename[:filename.find('.')]
#    f = codecs.open(htmlsource + '\\'+ fn + '.html',"r","iso8859_2")
#    text = BeautifulSoup(f, "html.parser").get_text(" ")
#    text = text[:text.find('The review')]
#    s = codecs.open(corpusdir + '\\' + fn + '.txt', 'w',"utf-8")
#    try:
#        s.write(text)
#    except UnicodeEncodeError as e:
#        s.close
#    f.close

# Using the annotated data from polarity to construct the classifier
tokenizer = RegexpTokenizer(r'\w+')
doc = []
with codecs.open("C:\\Users\\corrocherfilhonw\\workspace\\polarity\\reviewed\\rt-polarity.pos","r","iso8859_2") as f:
    for line in f:
        doc.append((tokenizer.tokenize(line),'pos'))
#        doc.append((nltk.word_tokenize(line),'pos'))
with codecs.open("C:\\Users\\corrocherfilhonw\\workspace\\polarity\\reviewed\\rt-polarity.neg","r","iso8859_2") as f:
    for line in f:
        doc.append((tokenizer.tokenize(line),'neg'))
#        doc.append((nltk.word_tokenize(line),'neg'))
random.seed(666)
random.shuffle(doc)

# Create the corpus for the movie review
my_corpus = nltk.corpus.PlaintextCorpusReader(corpusdir, '.*\.txt')

# Filter words
# from nltk.corpus import stopwords
# filtered_words = [word for word in my_corpu.words() if word not in stopwords.words('english')]

# Preparing the classifier
all_words = nltk.FreqDist(w.lower() for w in my_corpus.words())
word_features = list(w for w in all_words if w not in stopwords.words('english') and w.isalpha())[:3000]
# word_features = list(w for w in all_words)[:2000]

# Feature extractor
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

featuresets = [(document_features(d), c) for (d,c) in doc]
train_set, test_set = featuresets[:1000], featuresets[1000:]

# Bayes classifier
bayes_classifier = nltk.NaiveBayesClassifier.train(train_set)
start = timer()
print(nltk.classify.accuracy(bayes_classifier, test_set))
end = timer()
print (end - start) 


# Decision Tree classifier
dt_classifier = nltk.DecisionTreeClassifier.train(train_set)
start = timer()
print(nltk.classify.accuracy(dt_classifier, test_set))
end = timer()
print (end - start)

# Maximum entropy classifier
ent_classifier = nltk.MaxentClassifier.train(train_set, max_iter=3)
start = timer()
print(nltk.classify.accuracy(ent_classifier, test_set))
end = timer()
print (end - start)


# For each file
# fname = '0002' 
# f = codecs.open(htmlsource + '\\'+ fname + '.html',"r","iso8859_2")
# review = BeautifulSoup(f, "html.parser").get_text(" ").lower()
# review = review[:review.find('the review')]

# Tokenization
# review_tokens = nltk.tokenizer.tokenize(review)

# Part-of-Speech tagging (Unigram)
# Note: based on the approach for document classification
# POS tagging won't be used. It was left in the case another approach
# that uses POS classification may be used in the future
# brown_tagged_sents = brown.tagged_sents(categories='reviews')
# unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
# tagged_review = unigram_tagger.tag(review_tokens)

tokenizer = RegexpTokenizer(r'\w+')
wn = []
for filename in os.listdir(corpusdir):
    print(filename)
    fn = filename[:filename.find('.')]
    f = codecs.open(corpusdir + '\\'+ fn + '.txt',"r","utf-8")
    text = f.read()
    text = text[:text.find('The review')]
    t = tokenizer.tokenize(text)
    for w in t:
        if w not in stopwords.words('english'):
            wn.append(w)
    f.close()

# fq = nltk.FreqDist(w.lower() for w in my_corpus.words() if w.isalpha() and w not in stopwords.words('english'))

st = ' '.join(wn)
fn = 'filtered_words'
s = codecs.open(corpusdir + '\\' + fn + '.txt', 'w')
s.write(st)
s.close