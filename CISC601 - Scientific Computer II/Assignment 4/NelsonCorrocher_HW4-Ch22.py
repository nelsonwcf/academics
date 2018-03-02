from __future__ import division
import _numinteq
import _numint
import math
import _plot

print("Exercise 22.1")
print "------------------"


def f(x):
    return x * math.e ** (2 * x)
a = 0
b = 3

# Vectors
fn1 = (f(a+0*(b-a)/1), f(a+1*(b-a)/1))
fn2 = (f(a+0*(b-a)/2), f(a+1*(b-a)/2), f(a+2*(b-a)/2))
fn4 = (f(a+0*(b-a)/4), f(a+1*(b-a)/4), f(a+2*(b-a)/4), f(a+3*(b-a)/4), f(a+4*(b-a)/4))
fn8 = (f(a+0*(b-a)/8), f(a+1*(b-a)/8), f(a+2*(b-a)/8), f(a+3*(b-a)/8), f(a+4*(b-a)/8), f(a+5*(b-a)/8), f(a+6*(b-a)/8), f(a+7*(b-a)/8), f(a+8*(b-a)/8))

# Trapezoidal method results
print("For n = 1:")
ih1 = _numint.trapm(fn1, (b-a)/1, 1)
print ih1
print("For n = 2:")
ih2 = _numint.trapm(fn2, (b-a)/2, 2)
print ih2
print("For n = 4:")
ih4 = _numint.trapm(fn4, (b-a)/4, 4)
print ih4
print("For n = 8:")
ih8 = _numint.trapm(fn8, (b-a)/8, 8)
print ih8
print

# Combining the results
print("O(h^4)")
a = (4/3) * ih2 - (1/3) * ih1
print a
b = (4/3) * ih4 - (1/3) * ih2
print b
c = (4/3) * ih8 - (1/3) * ih4
print c
print

print("O(h^6)")
d = (16/15) * b - (1/15) * a
print d
e = (16/15) * c - (1/15) * b
print e
print

print("O(h^8)")
f = (64/63) * e - (1/63) * d
print f
print

print("Error comparison:")
true_value = (1 / 4) * (1 + 5 * math.e ** 6)
print("Trapezoidal( n = 8 ):" + str(abs(ih8 - true_value)))
print("Romberg( O(h^8) ):" + str(abs(f - true_value)))

print
print
print("Exercise 22.3")
print "------------------"


def f(x):
    return (math.e ** x * math.sin(x)) / (1 + x ** 2)
a = 0
b = 2

print(_numinteq.romberg(f, a, b, debug=True))
print ("vs trapezoidal method with (n = 8):")
fn8 = (f(a+0*(b-a)/8), f(a+1*(b-a)/8), f(a+2*(b-a)/8), f(a+3*(b-a)/8), f(a+4*(b-a)/8), f(a+5*(b-a)/8), f(a+6*(b-a)/8), f(a+7*(b-a)/8), f(a+8*(b-a)/8))
x = _numint.trapm(fn8, (b-a)/8, 8)
print x
print ("TRUE VALUE: 1.94013")

print
print "Summary"
print "------------------"
print ("Most of this chapter revolves around showing more efficient methods in computing the value of integrals.")
print ("Looking at the pseudocode, we can see that Romberg computations involve calling the trapezoidal method")
print ("plus additional steps so each iteration is more computationally complex than the trapezoidal method.")
print ("However, as it was seen in exercises one and three, eight iterations of the trapezoidal method provides")
print ("a bigger error than just four or three iterations of Romberg method.")
print ("One important thing is that it is still not clear to me is if Romberg is indeed faster in all cases.")
print ("Trapezoidal algorithm is of complexity O(n), n being the number of equally distributed intervals.")
print ("Romberg seems to be of quadratic complexity but the number of iterations are dependent on the error, not on n.")
print ("For a certain error E, as long as Romberg algorithm iterations are less than Log n to obtain an error less or equal")
print ("to E, n being the number of iterations for the trapezoidal method to obtain the same or lower error than E, we can")
print ("affirm that Romberg is indeed faster.")




