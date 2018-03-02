# -*- coding: utf-8 -*-
"""
Created on Sun May 14 20:17:32 2017

@author: Nelson Corrocher
@nltk_version: 3.6.1
@python_version: 3.6
"""

import nltk

# Exercise 1

read_expr = nltk.sem.Expression.fromstring

# a. If [Angus sings], it is not the case that [Bertie sulks].
read_expr('A -> -B')

# b. [Cyril runs] and [barks].
read_expr('A & B')

# c. [It will snow] if [it doesn’t rain].
read_expr('A -> -B')

# d. It’s not the case that [Irene will be happy] if [Olive or [Tofu comes]].
read_expr('-A -> B | C')

# e. [Pat didn’t cough] or [sneeze].
read_expr('-A | -B')

# f. If [you don’t come] if [I call], [I won’t come] if [you call].
read_expr('(-A -> B) -> (-C -> D)')

# Exercise 2

# a. Angus likes Cyril and Irene hates Cyril.
read_expr('like(angus, cyril) & hate(irene,cyril)')

# b. Tofu is taller than Bertie
read_expr('taller(tofu, bertie)')

# c. Bruce loves himself and Pat does too.
read_expr('love(bruce, bruce) & love(pat,bruce)')

# d. Cyril saw Bertie, but Angus didn’t.
read_expr('see(cyril, bertie) & -see(angus,bertie)')

# e. Cyril is a four-legged friend.
read_expr('four_legged(cyril)')

# f. Tofu and Olive are near each other.
read_expr('near(tofu, olive) & near(olive, tofu)')

# Exercise 3

# a. Angus likes someone and someone likes Julia.
read_expr('exists x. (like(angus, x) & like(x, julia))')

# b. Angus loves a dog who loves him.
read_expr('exists x. (dog(x) & like(angus, x) & like(x, angus))')

# c. Nobody smiles at Pat.
read_expr('-all x. (smile(x, Pat))')

# d. Somebody coughs and sneezes.
read_expr('exists x. (cough(x) | sneeze(x))')

# e. Nobody coughed or sneezed.
read_expr('-all x. (cough(x) | sneeze(x))')

# f. Bruce loves somebody other than Bruce.
read_expr('exists x. (-bruce(x) & love(bruce, x))')

# g. Nobody other than Matthew loves Pat.
read_expr('all x. (-matthew(x) -> -love(x,pat))')

# h. Cyril likes everyone except for Irene.
read_expr('all x. (-irene(x) -> like(cyril, x))')

# i. Exactly one person is asleep.
read_expr('exists x. (sleep(x) & -all y. (sleep(y) -> y != x))')

# Exercise 4

# a. feed Cyril and give a capuccino to Angus
read_expr('\\x. (feed(x,cyril) & give_cappucino(x,angus))')

# b. be given ‘War and Peace’ by Pat
read_expr('\\x. (givebook(pat,x))')

# c. be loved by everyone
read_expr('\\x. all y. (person(y) -> love(y,x))')

# d. be loved or detested by everyone
read_expr('\\x. all y. (person(y) -> love(y,x) | detest(y,x))')

# e. be loved by everyone and detested by no-one
read_expr('\\x. all y. (person(y) -> love(y,x) & -detest(y,x))')

# Exercise 5

# a1.
e1 = read_expr('\\x exists y. (love(x,y))')
e2 = read_expr('pat')
e3 = nltk.sem.ApplicationExpression(e1, e2)
print(e3.simplify())

# a2.
e1 = read_expr('\\x exists y. (love(x,y) | love(y,x))')
e2 = read_expr('pat')
e3 = nltk.sem.ApplicationExpression(e1, e2)
print(e3.simplify())

# a3.
e1 = read_expr('\\x exists y. (love(x,y) | love(y,x))')
e2 = read_expr('pat')
e3 = nltk.sem.ApplicationExpression(e1, e2)
print(e3.simplify())

# a4.
e1 = read_expr('\\x. walk(fido)')
e2 = read_expr('pat')
e3 = nltk.sem.ApplicationExpression(e1, e2)
print(e3.simplify())