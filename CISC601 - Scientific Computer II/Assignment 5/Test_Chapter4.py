from __future__ import division
import _numinteq
import _numint
import math
import _plot

print("Exercise 23.1")
print("------------------")


def f(x):
    return -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2


def f2(x):
    return -0.4*x**3 - 0.45*x**2 - 1.0*x - 0.25

c = 0.5
h = 0.25
tv = f2(c)
print("True value of f2(xi): " + str(tv))
print("xi: " + str(c))
print("h: " + str(h))
print


def ffh(x, h):
    return (f(x+h) - f(x))/h


def ffh2(x, h):
    return (-f(x+2*h) + 4 * f(x+h) - 3*f(x)) / (2*h)


def fbh(x, h):
    return (f(x) - f(x - h))/h


def fbh2(x, h):
    return (3 * f(x) - 4 * f(x - h) + f(x - 2*h)) / (2*h)


def fch2(x, h):
    return (f(x+h) - f(x-h)) / (2*h)


def fch4(x, h):
    return (-f(x+2*h) + 8*f(x+h) - 8*f(x-h) + f(x-2*h)) / (12*h)


def foh(x, h):
    return tv-ffh(x, h)


def foh2(x, h):
    return tv-ffh2(x, h)


def boh(x, h):
    return tv-fbh(x, h)


def boh2(x, h):
        return tv-fbh2(x, h)


def coh(x, h):
    return tv-fch2(x, h)


def coh2(x, h):
    return tv-fch4(x, h)




print("Forward approximation:")
print(str(ffh(c,h)))
et = abs(round(100 * (ffh(c,h) - tv) / tv,1))
print("Error: " + str(et) + "%")
print

print("Backward approximation:")
print(str(fbh(c,h)))
et = abs(round(100 * (fbh(c,h) - tv) / tv,1))
print("Error: " + str(et) + "%")
print

print("centered approximation:")
print(str(fch2(c,h)))
et = abs(round(100 * (fch2(c,h) - tv) / tv,1))
print("Error: " + str(et) + "%")

