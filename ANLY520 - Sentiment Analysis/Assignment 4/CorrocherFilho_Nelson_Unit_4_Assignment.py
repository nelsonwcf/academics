import nltk

# Exercise 3

sentence = "They wind back the clock, while we chase after the wind."
tokens = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(tokens)
print [nltk.help.upenn_tagset(w) for (_, w) in tags]

# Exercise 5
d = {}
type(d)

d['dragon'] = 'green'
# print d['tiger'] - Causes an error because tiger is not in the dict

d = {'dragon': 'green', 'tiger': 'yellow', 'phoenix': 'orange'}

# To address the not-in-the-dict problem, we can use defaultdict

d = nltk.defaultdict(str, {'dragon': 'green', 'tiger': 'yellow', 'phoenix': 'orange'})
print d['dragon']
print d['ki-rin'] # Now it doesn't cause an error

# Exercise 6

d = {'dragon': 'green', 'tiger': 'yellow', 'phoenix': 'orange'}
del d['dragon']
# print d['dragon'] - If we try to address it, there will be an error

d = nltk.defaultdict(str, {'dragon': 'green', 'tiger': 'yellow', 'phoenix': 'orange'})
del d['dragon']
print d # Also works for defaultdict.

# Exercise 7

d1 = {'dragon': 'green', 'tiger': 'yellow', 'phoenix': 'orange'}
d2 = {'tarrasque': 'brown', 'mind-flayer':'blue', 'dragon': 'golden'}
d1.update(d2)
print d1

# d1.update(d2) brings all elements from d2 into d1. If there is a repeated element in d2, it overwrites d1 value.
# There are many uses for it and it is not restricted to language processing. In the context of language processing,
# it could be useful when you have one dictionary with only nouns and another one with verbs and you would like to
# merge to two for the creation of the tagset. The case in which the same entry is on both list would need to be
# addressed, for example to correct a match or two include both tags to the key.

# Exercise 10

from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents()
brown_sents = brown.sents(categories='news')
from nltk.corpus import gutenberg
guten_sents = gutenberg.sents()
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
print unigram_tagger.tag(guten_sents[1212])

# One reason for some words be classified as None is because they didn't appear in the training set before (hapax)
# thus the N-Gram classifier don't know about it.