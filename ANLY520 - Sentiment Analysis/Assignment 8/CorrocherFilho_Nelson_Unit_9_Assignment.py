import nltk

# Question 1

# You need some way to extend the grammar (tense agreement, in this example). While this could have been done using the
# previously introduced tools, this chapter introduces the concept of using feature structure to match tenses, grammar
# categories, etc.

# Grammar solution from (8)

grammar8 = ("""
    S -> NP_3RD VP_3RD
    S -> NP_1ST VP_1ST
    NP_3RD -> N_3RD ADJ
    NP_1ST -> N_1ST ADJ
    VP_3RD -> V_3RD
    VP_1ST -> V_1ST
    ADJ -> 'happy'
    N_3RD -> 'she'
    N_1ST -> 'I'
    V_3RD -> 'is'
    V_1ST -> 'am'
""")

# Grammar solution from (20)

grammar20 = ("""
    S -> NP[AGR=?n] VP[AGR=?n]
    NP[AGR=?n] -> PropN[AGR=?n]
    VP[TENSE=?t, AGR=?n] -> Cop[TENSE=?t, AGR=?n] Adj
    Cop[TENSE=pres, AGR=[NUM=sg, PER=3]] -> 'is'
    Cop[TENSE=pres, AGR=[NUM=sg, PER=1]] -> 'am'
    PropN[AGR=[NUM=sg, PER=3]] -> 'she'
    PropN[AGR=[NUM=sg, PER=1]] -> 'I'
    Adj -> 'happy'
""")

# Question 2

grammar = ("""
    % start S
    S -> NP[COUNT=?n] VP[COUNT=?n]
    
    NP[COUNT=?n] -> N[COUNT=?n]
    NP[COUNT=?n] -> Det[COUNT=?n] N[COUNT=?n]
    NP[COUNT=pl] -> N[COUNT=pl]
    
    VP[COUNT=?n] -> IV[COUNT=?n]
    VP[COUNT=?n] -> TV[COUNT=?n] ADJ
    
    Det -> 'the'
    N[COUNT=sg] -> 'boy' | 'water'
    N[COUNT=pl] -> 'boys'
    IV[COUNT=sg] -> 'sing'
    IV[COUNT=pl] -> 'sings'
    TV[COUNT=sg] -> 'is'
    ADJ -> 'precious'
""")

# Question 3

# My understanding is that if fs1 subsumes fs2, then fs2.unify(fs1) is equal to fs2. Using this logic,
# I coded the function below:


def subsumes(fs1, fs2):
    if fs2 == fs2.unify(fs1):
        return True
    else:
        return False

# Testing it
fs1 = nltk.FeatStruct(NUMBER=74)
fs2 = nltk.FeatStruct(NUMBER=74, STREET='rue Pascal')
print subsumes(fs1, fs2)  # Should return true

fs1 = nltk.FeatStruct(NUMBER=74, CITY='LA')
fs2 = nltk.FeatStruct(NUMBER=74, STREET='rue Pascal')
print subsumes(fs1, fs2)  # Should return false

# Question 4

# Obs: I spent more time in this question than in the other four (including understand exercise 3).
# The book is particularly bad at explaining the hierarchy of verbs for phrasal projection, so
# I will have to guess. SUBCAT=clause should be the zero projection. SUBCAT=trans verbs should have either one or
# two bars. SUBCAT=Intrans verbs are probably head children.
# Not sure if my difficulty for understanding this concept is an English language barrier or a simply a
# hideously bad book.
# Example: "John told Mary that he brought Fran to swim at the lake".
# -- told is SUBCAT=clause, brought is SUBCAT=trans and swim is SUBCAT=intrans
# I'm going to use that logic here but I have no idea if what I'm doing is correct.

grammar = ("""
    VP[TENSE=?t, NUM=?n] -> V[SUBCAT=intrans, TENSE=?t, NUM=?n, BAR=2]
    VP[TENSE=?t, NUM=?n] -> V[SUBCAT=trans, TENSE=?t, NUM=?n, BAR=<1,2>] NP
    VP[TENSE=?t, NUM=?n] -> V[SUBCAT=clause, TENSE=?t, NUM=?n, BAR=0] SBar
    
    V[SUBCAT=intrans, TENSE=pres, NUM=sg, BAR=2] -> 'disappears' | 'walks'
    V[SUBCAT=trans, TENSE=pres, NUM=sg, BAR=<1,2>] -> 'sees' | 'likes'
    V[SUBCAT=clause, TENSE=pres, NUM=sg, BAR=0] -> 'says' | 'claims'
    
    V[SUBCAT=intrans, TENSE=pres, NUM=pl, BAR=2] -> 'disappear' | 'walk'
    V[SUBCAT=trans, TENSE=pres, NUM=pl, BAR=<1,2>] -> 'see' | 'like'
    V[SUBCAT=clause, TENSE=pres, NUM=pl, BAR=0] -> 'say' | 'claim'
    
    V[SUBCAT=intrans, TENSE=past, BAR=2] -> 'disappeared' | 'walked'
    V[SUBCAT=trans, TENSE=past, BAR=<1,2>] -> 'saw' | 'liked'
    V[SUBCAT=clause, TENSE=past, BAR=0] -> 'said' | 'claimed
""")

# Question 5

# For the sake of cleanliness, showing just the modified lines (added a SUBCAT category to verbs)

grammar = ("""
# Grammar Productions
VP[AGR=?a] -> V[SUBCAT=intrans, AGR=?a]
VP[AGR=?a] -> V[SUBCAT=trans, OBJCASE=?c, AGR=?a] NP[CASE=?c]

# Verbs
V[SUBCAT=intrans, AGR=[NUM=sg,PER=1]] -> 'komme'
V[SUBCAT=intrans, AGR=[NUM=sg,PER=2]] -> 'kommst'
V[SUBCAT=intrans, AGR=[NUM=sg,PER=3]] -> 'kommt'
V[SUBCAT=intrans, AGR=[NUM=pl, PER=1]] -> 'kommen'
V[SUBCAT=intrans, AGR=[NUM=pl, PER=2]] -> 'kommt'
V[SUBCAT=intrans, AGR=[NUM=pl, PER=3]] -> 'kommen'
V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=sg,PER=1]] -> 'sehe' | 'mag'
V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=sg,PER=2]] -> 'siehst' | 'magst'
V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=sg,PER=3]] -> 'sieht' | 'mag'
V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=sg,PER=1]] -> 'folge' | 'helfe'
V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=sg,PER=2]] -> 'folgst' | 'hilfst'
V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=sg,PER=3]] -> 'folgt' | 'hilft'
V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=pl,PER=1]] -> 'sehen' | 'moegen'
V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=pl,PER=2]] -> 'sieht' | 'moegt'
V[SUBCAT=trans, OBJCASE=acc, AGR=[NUM=pl,PER=3]] -> 'sehen' | 'moegen'
V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=pl,PER=1]] -> 'folgen' | 'helfen'
V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=pl,PER=2]] -> 'folgt' | 'helft'
V[SUBCAT=trans, OBJCASE=dat, AGR=[NUM=pl,PER=3]] -> 'folgen' | 'helfen'
""")
