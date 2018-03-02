# Before anything else, feedback on this chapter:
# This book is not very good overall but this chapter was particularly bad.
# Dense and with lots of information but all over the place; three of the requested
# exercises cannot be solved with information from just this and previous chapters.
# Since this version is somewhat deprecated, the website is not user friendly for people
# using the old version of the book. Exercise 3 is complex and it involves more work than
# all other assignments together so far - and the information for using it correctly is not
# in the book and not even in the site. Had to use external resources and I don't even
# know if it is correct or not.


from nltk.corpus import names, senseval, movie_reviews
import nltk
import random
import numpy as np


# QUESTION 1

# I read more about word sense disambiguation and found few references that shows
# the amount of annotated data for training. The one reference I can point is in
# this URL (http://web.eecs.umich.edu/~mihalcea/papers/mihalcea1.acl05.pdf) and
# is part of the research for the algorithm used by a certain software that was
# not available at the time of this assignment. They used an annotated data of
# between 36k to 208k words, depending on the model to achieve precision in order
# of the 65%. I believe that such amount of data may be required due to the ambiguous
# nature of spoken and written language, as there are cases in that even humans can't
# understand correctly and we try to classify everything based on similarity.
# Additionally, This problem may be computationally hard because
# we still can't copy the process the brain uses to resolve ambiguity.

# QUESTION 2


# Tested many features by just changing this function
# Left the one with the highest ratio. Note: since the data is shuffled
# results will likely change between executions.
def gender_features(word):
    features = {'last_letter': word[-1], 'first_letter': word[0], 'length': len(word), 'suffix2': word[-2:]}
    return features


# For dev-test:
# Current precision: 0.791
# Previous precisions: 0.760, 0.770, 0.776,

names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])

l = []

for i in range(0, 300):
    random.shuffle(names)

    test_raw = names[:500]
    dev_test_raw = names[500:1500]
    training_raw = names[1500:]

    train_set = [(gender_features(n), g) for (n, g) in training_raw]
    dev_test_set = [(gender_features(n), g) for (n, g) in dev_test_raw]
    test_set = [(gender_features(n), g) for (n, g) in test_raw]
    classifier = nltk.NaiveBayesClassifier.train(train_set)

    l.append(nltk.classify.accuracy(classifier, test_set))

# Necessary to avoid fluctuations from the shuffle function
print np.mean(l)

# QUESTION 3

# I couldn't do this question correctly for the lack of resources.
# The book is never descriptive on what each code line does,
# always showing what to do (not why). So far, I was able to learn,
# from the example and customize it based on research. For this exercise,
# however, it doesn't give any example in how to do that and refers
# to a page back in the site. However, this page doesn't exist anymore
# because the edition of the book is old. The new page mentions how to
# work with the Lesk algorithm which in not even mentioned in the book.
# Since I can't run the exercise, the second best thing I can do is to
# describe what my steps would be:

# 1. Using senseval corpus, I would create trigrams on the word hard,
# from one word before and one word after, while keeping the lexical categories and
# adding the meaning in the end:
# Example: {((a, AT), (hard, ADJ), (plank, NN)), 'HARD3'}

# 2. Next step is to modify this construct to something like: {(AT, ADJ, NN),'HARD3'}
# This is the database for our feature selection

# 3. Create a function that, given a corpus, searches for the word 'hard' and create a
# similar construct like the previous example (will have to tag the relevant words).
# This is function searched the dataset from 2 for the same construct as the one
# generated in this step. This our effective FEATURE EXTRACTOR.

# 4. Now we look at any corpus and generate a tuple based on the word hard, its previous
# and after words as well, like {(AT, ADJ, NN)} and we can use the classifier to judge
# it.

# Obs: I'm using only trigrams and this method already requires a lot of word tuples for
# training. If we assume 20 different lexical categories, we will have 8000 possible combinations
# for each. Complexity of n^n. This may explain why word sense disambiguation is such a hard
# problem.

# EXERCISE 4

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]


def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


featuresets = [(document_features(d), c) for (d, c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

classifier.show_most_informative_features(30)

# Some of them seem to be obvious like 'lame', 'worst' and 'waste' for negative
# and 'outstanding', 'wonderfully', 'superb'. They can be considered informative
# because most people who uses them uses them in a clear context. For example,
# it would be unusual for someone to call a movie outstanding in a bad review.
# However, this is not decisive because, for example, one reviewer could be making
# a comparison between the 'oustanding' performance of the main actor in the previous
# movie while being 'mediocre' in the current one.
# Some of the features are indeed surprising, like 'seagal' being a negative indicator,
# 'damon' being a positive indicator. Other interesting ones are 'jedi' and 'sandler'.

# EXERCISE 5

# Let's use the first one for the sake of simplicity in the exercise.

from nltk.corpus import names


def gender_features(word):
    return {'last_letter': word[-1]}


# Taking out shuffle, results are much worse, probably because they list of names is sorted by male and female
names = ([(name, 'male') for name in names.words('male.txt')] +
         [(name, 'female') for name in names.words('female.txt')])

random.shuffle(names)

test_raw = names[:1000]
training_raw = names[1000:]

train_set = [(gender_features(n), g) for (n, g) in training_raw]
test_set = [(gender_features(n), g) for (n, g) in test_raw]

# Naive Bayes classifier
b_classifier = nltk.NaiveBayesClassifier.train(train_set)
print nltk.classify.accuracy(b_classifier, test_set)
# Precision: 0.755

# Decision Trees classifier
dt_classifier = nltk.DecisionTreeClassifier.train(train_set)
print nltk.classify.accuracy(dt_classifier, test_set)
# Precision: 0.757

# Maximum Entropy classifier, which is only mentioned on Chapter 7
ent_classifier = nltk.MaxentClassifier.train(train_set, max_iter=10)
print nltk.classify.accuracy(ent_classifier, test_set)
# Precision: 0.757

# Their performance is quite close for the features extractor I used and the size of
# this sample (Bayes is slightly less precise)
