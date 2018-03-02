from __future__ import division
import _numinteq
import _numint
import math
import _plot
import _ode

print("Exercise 25.1")
print("------------------")

print("a) Analytically")


def y(t):
    return math.e**(-1.1*t + (t**3)/3)*1

print("t = 0" + str(y(0)))
print("t = 2" + str(y(2)))
print
print("b) Euler")
h1 = 0.5
h2 = 0.25


