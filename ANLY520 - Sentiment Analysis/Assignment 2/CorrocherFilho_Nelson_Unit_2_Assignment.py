# Exercise 1
phrase = ['orange', 'grape', 'lemon', 'lime', 'papaya', 'apple', 'strawberry']
phrase2 = ['pineapple', 'kiwi', 'mango', 'coconut', 'blueberry']

print(phrase + phrase2)

print(phrase * 2)
print '\n'

for n in phrase[0:3]:
    print n,
print '\n'

print(sorted(phrase))

# Exercise 2
import nltk

print ('\n'),
austen = nltk.corpus.gutenberg.words('austen-persuasion.txt')
print(len(austen))
print(len(set(austen)))

# Exercise 3
from nltk.corpus import brown

cat = ['lore','adventure']
for w in brown.fileids():
    print brown.words(w)[:50]
    print '\n',

# Exercise 4
from nltk.corpus import state_union

su = state_union.words()
myCorpus = nltk.Text(su)

print(myCorpus.count("men"))
print(myCorpus.count("women"))
print(myCorpus.count("people"))


myCorpus.dispersion_plot(['men', 'women', 'people']) # Need to be closed for the application to continue

# Exercise 5
from nltk.corpus import wordnet as wn

lake = wn.synset('lake.n.01')
print(lake.member_meronyms())
print(lake.substance_meronyms())
print(lake.part_meronyms())
print(lake.member_holonyms())
print(lake.substance_holonyms())
print(lake.part_holonyms())

atom = wn.synset('atom.n.01')
print(atom.member_meronyms())
print(atom.substance_meronyms())
print(atom.part_meronyms())
print(atom.member_holonyms())
print(atom.substance_holonyms())
print(atom.part_holonyms())

earth = wn.synset('earth.n.01')
print(earth.member_meronyms())
print(earth.substance_meronyms())
print(earth.part_meronyms())
print(earth.member_holonyms())
print(earth.substance_holonyms())
print(earth.part_holonyms())

crumbs = wn.synset('crumbs.n.01')
print(crumbs.member_meronyms())
print(crumbs.substance_meronyms())
print(crumbs.part_meronyms())
print(crumbs.member_holonyms())
print(crumbs.substance_holonyms())
print(crumbs.part_holonyms())