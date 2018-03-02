# Question 1

# Without the B, there wouldn't be any way to knowing to which chunk a token belongs to (where one ends and another begins).

# Question 2

# many/JJ researchers/NNS
# two/CD weeks/NNS
# both/DT new/JJ positions/NNS

# {[<DT><JJ><CD>]?<JJ>*<NN>}

# Question 3

import nltk
from nltk.corpus import conll2000

print conll2000.chunked_sents(chunk_types=['NP'])[0]
print conll2000.chunked_sents(chunk_types=['NP'])[1]
print conll2000.chunked_sents(chunk_types=['NP'])[2]

sample = conll2000.chunked_sents(chunk_types=['NP'])

grammar = r"NP: {<[CDJNP].*>+}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(sample)

grammar = r"NP: {<DT>?<POS|VBN|JJ.*>*<NN.*>+}"
cp = nltk.RegexpParser(grammar)
print cp.evaluate(sample)

# Based on the sample I evaluated, the main problem for me was that when the precision went up,
# the IOB Accuracy went down. I don't know if this is the main difficult most NLP researchers face
# but in some complex nouns, many nouns chain up and it is difficult to know which ones belong
# to which chunk (avoiding overlap).

# Question 4

grammar = r"""
  NP:
    {<.*>+}          # Chunk everything
    }<VBD|IN>+{      # Chink sequences of VBD and IN
  """
cp = nltk.RegexpParser(grammar)
print cp.evaluate(sample)

grammar = r"""
  NP:
    {<.*>+}                 # Chunk everything
    }<VB.*|IN|TO|CC>+{      # Chink sequences of VB*s, INs, TOs and CCs, which seems more often excluded from chunks
  """
cp = nltk.RegexpParser(grammar)
print cp.evaluate(sample)

# While I could make some significant improvements in the chinking strategy compared to the one showed in the book, it
# was still not good enough as chunking (lower score) at least for simple RegExes.

# Question 5

# Just based on exercise text, I can see where this may go: gerund nouns and participle adjectives have the same
# structure ending in ing.

import nltk
from nltk.corpus import brown

# I'm not very good at tagging english grammar so I'm going to use nltk libraries for that.

# For some reason, the line below crashes and doesn't execute. Either I'm doing something wrong or this is a bug in the parser.
# tokens = nltk.word_tokenize("The eating of the grapes did not help managing her condition while the knights were leading the king to something dark. The forming of a sentence involves a lot of guessing.".lower())
tokens = nltk.word_tokenize(
    "The eating of the grapes did not help managing her condition while the walking knights were leading the king to something dark.".lower())
train_data = brown.tagged_sents(categories=["romance", "news"])
tagger = nltk.UnigramTagger(train_data)
sentence = tagger.tag(tokens)

grammar = r"""
  NP:
    {<DT>*<VBG><NN.*>*}
    {<NN.*>*<VBG><NN.*>*}
  """
cp = nltk.RegexpParser(grammar)
print cp.parse(sentence)
