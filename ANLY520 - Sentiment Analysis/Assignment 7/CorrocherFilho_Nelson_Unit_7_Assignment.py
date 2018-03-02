import nltk
import nltk.tree

# Question 3

grammar = nltk.parse_cfg("""
    S -> CS
    CS -> NP VP | CS CNJ CS
    VP -> VI
    NP -> "Kim" | "Dana" | "everyone"
    VI -> "arrived" | "left" | "cheered"
    CNJ -> "and" | "or"
    """)

phrase = "Kim arrived or Dana left and everyone cheered".split()
parser = nltk.ChartParser(grammar)
trees = parser.nbest_parse(phrase)
for tree in trees:
    print tree

# The code below would plot the trees created from phrase but for some reason the method plot() halts the
# execution, reason it was commented below.
# for tree in trees:
#    tree.draw()

# Question 4

help(nltk.tree)
# Reading the help using the help() function in python so far has not been very useful. It is better to look the API
# directly in the website: http://www.nltk.org/api/nltk.html?highlight=tree#module-nltk.tree

# Recovering the original phrase:
print tree[0].flatten()

# Some other methods don't work with NLTK 2.0 package, like Tree.fromstring(t) so I can't really test many
# of the functions there.

# Question 5

# Part a
grammar = nltk.parse_cfg("""
    S -> CS
    CS -> NP | NP CNJ NP
    NP -> P | ADJ P
    P -> "men" | "women" | P CNJ P
    ADJ -> "old"
    CNJ -> "and"
    """)

phrase = "old men and women".split()
parser = nltk.ChartParser(grammar)
trees = parser.nbest_parse(phrase)
for tree in trees:
    tree.draw()

# Part b
# This exercise is unclear on what it wants and the documentation of the API in the site is based on the NLTK 3.0.
# Couldn't find the correct input format for the nltk.Tree() class. I'm going to use the same method I used before
# and then show the tree instead for a phrase that is in the chapter.
grammar = nltk.parse_cfg("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")

phrase = "I shot an elephant in my pajamas".split()
parser = nltk.ChartParser(grammar)
trees = parser.nbest_parse(phrase)
for tree in trees:
    print tree
    tree.draw()

# Part c
grammar = nltk.parse_cfg("""
S -> CS
CS -> NP VP 
VP -> V NP | V NP AP
NP -> DET N | N
AP -> DTime N
N -> "woman" | "man" | "Thursday"
V -> "saw"
DET -> "The" | "a"
DTime -> "last"
""")

phrase = "The woman saw a man last Thursday".split()
parser = nltk.ChartParser(grammar)
trees = parser.nbest_parse(phrase)
for tree in trees:
    tree.draw()

# Question 7

sent = "In after-years he liked to think" \
       " that he had been in Very Great Danger during the Terrible Flood, but the only danger he had really been in" \
       " was the last half-hour of his imprisonment, when Owl, who had just flown up, sat on a branch of his tree" \
       " to comfort him, and told him a very long story about an aunt who had once laid a seagull’s egg by mistake," \
       " and the story went on and on, rather like this sentence, until Piglet who was listening out of his window" \
       " without much hope, went to sleep quietly and naturally, slipping slowly out of the window towards the" \
       " water until he was only hanging on by his toes, at which moment, luckily, a sudden loud squawk from Owl," \
       " which was really part of the story, being what his aunt said, woke the Piglet up and just gave him time to" \
       " jerk himself back into safety and say, “How interesting, and did she?” when—well, you can imagine his joy" \
       " when at last he saw the good ship, Brain of Pooh (Captain, C. Robin; 1st Mate, P. Bear) coming over the sea" \
       " to rescue him…"

import nltk

grammar = nltk.parse_cfg("""
S -> S1
S1 -> S2 | S1 CNJ S1
S2 -> "S"
CNJ -> "when" | "but" | "and" | "until"
""")

phrase = "S but S when S and S and S until S until S when S when S".split()
parser = nltk.ChartParser(grammar)
trees = parser.nbest_parse(phrase)
for tree in trees:
    print tree

# Seems like the main syntactic constructions used for long sentences are conjunctions.

# Question 8

nltk.app.rdparser()
# If you just change the sentence in this app, it most likely won't work. You also have to change the grammar
# of the left window. I can't find an easy way to post the animation showing what the app was doing. One thing I
# noticed (using "the dog saw a man in the park" sentence) is that even for a simple sentence with a simple grammar,
# the recursion take a lot of steps. I have to think a bit more in the efficiency of this parser, but so far it looks
# impractical for anything bigger than a longer sentence (I could be wrong; have to play with it a bit more).
