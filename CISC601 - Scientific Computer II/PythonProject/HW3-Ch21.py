from __future__ import division
import _numint
import _numint2
import math

print("EXERCISE 21.4")
print("Analytically: ")
print("x^3/3 + 4x - 4/x | [1,2]")
print("= 25/3 = ", 25/3)
print
print("Using the algorithm: ")


def f(x):
    return (x + 2. / x) ** 2
#def f(x):
#    return 0.2 + 25 * x - 200 * x ** 2 + 675 * x ** 3 - 900 * x ** 4 + 400 * x ** 5

a = 1
b = 2
true = 25 / 3
# a = 0
# b = 0.8

# Vectors
fn1 = (f(a+0*(b-a)/1), f(a+1*(b-a)/1))
fn2 = (f(a+0*(b-a)/2), f(a+1*(b-a)/2), f(a+2*(b-a)/2))
fn3 = (f(a+0*(b-a)/3), f(a+1*(b-a)/3), f(a+2*(b-a)/3), f(a+3*(b-a)/3))
fn4 = (f(a+0*(b-a)/4), f(a+1*(b-a)/4), f(a+2*(b-a)/4), f(a+3*(b-a)/4), f(a+4*(b-a)/4))
fn5 = (f(a+0*(b-a)/5), f(a+1*(b-a)/5), f(a+2*(b-a)/5), f(a+3*(b-a)/5), f(a+4*(b-a)/5), f(a+5*(b-a)/5))

print("For n = 1:")
print(_numint.trapm(fn1, (b-a)/1, 1))
print("Error as percentage of precise value: " + str(math.fabs((true - _numint.trapm(fn1, (b-a)/1, 1))/_numint.trapm(fn1, (b-a)/1, 1))) + "%")
print
print("For n = 2:")
print(_numint.trapm(fn2, (b-a)/2, 2))
print("Error as percentage of precise value: " + str(math.fabs((true - _numint.trapm(fn2, (b-a)/2, 2))/_numint.trapm(fn2, (b-a)/2, 2))) + "%")
print
print("For n = 3:")
print(_numint.trapm(fn3, (b-a)/3, 3))
print("Error as percentage of precise value: " + str(math.fabs((true - _numint.trapm(fn3, (b-a)/3, 3))/_numint.trapm(fn3, (b-a)/3, 3))) + "%")
print
print("For n = 4:")
print(_numint.trapm(fn4, (b-a)/4, 4))
print("Error as percentage of precise value: " + str(math.fabs((true - _numint.trapm(fn4, (b-a)/4, 4))/_numint.trapm(fn4, (b-a)/4, 4))) + "%")
print
print("For n = 5:")
print(_numint.trapm(fn5, (b-a)/5, 5))
print("Error as percentage of precise value: " + str(math.fabs((true - _numint.trapm(fn5, (b-a)/5, 5))/_numint.trapm(fn5, (b-a)/5, 5))) + "%")
print

print("EXERCISE 21.5");
print("Analytically: ")
print("16x^4 - 48x^3 + 54x^2 - 27x + 81/16 | [-3,5]")
print("= 2056")
print
print("Using the algorithm: ")


def f(x):
    return (4*x - 3) ** 3
#def f(x):
#    return 0.2 + 25 * x - 200 * x ** 2 + 675 * x ** 3 - 900 * x ** 4 + 400 * x ** 5

a = -3
b = 5
true = 2056

# Vectors

fn4 = (f(a+0*(b-a)/4), f(a+1*(b-a)/4), f(a+2*(b-a)/4), f(a+3*(b-a)/4), f(a+4*(b-a)/4))
fn5 = (f(a+0*(b-a)/5), f(a+1*(b-a)/5), f(a+2*(b-a)/5), f(a+3*(b-a)/5), f(a+4*(b-a)/5), f(a+5*(b-a)/5))
fn6 = (f(a+0*(b-a)/6), f(a+1*(b-a)/6), f(a+2*(b-a)/6), f(a+3*(b-a)/6), f(a+4*(b-a)/6), f(a+5*(b-a)/6), f(a+6*(b-a)/6))
fn7 = (f(a+0*(b-a)/7), f(a+1*(b-a)/7), f(a+2*(b-a)/7), f(a+3*(b-a)/7), f(a+4*(b-a)/7), f(a+5*(b-a)/7), f(a+6*(b-a)/7), f(a+7*(b-a)/7))

print("For n = 4:")
print(_numint2.simpint(fn4, a, b, 4))
print("Error as percentage of precise value: " + str(math.fabs((true - _numint2.simpint(fn4, a, b, 4))/_numint2.simpint(fn4, a, b, 4))) + "%")
print
print("For n = 5:")
print(_numint2.simpint(fn5, a, b, 5))
print("Error as percentage of precise value: " + str(math.fabs((true - _numint2.simpint(fn5, a, b, 5))/_numint2.simpint(fn5, a, b, 5))) + "%")
print
print("For n = 6:")
print(_numint2.simpint(fn6, a, b, 6))
print("Error as percentage of precise value: " + str(math.fabs((true - _numint2.simpint(fn6, a, b, 6))/_numint2.simpint(fn6, a, b, 6))) + "%")
print
print("For n = 7:")
print(_numint2.simpint(fn7, a, b, 7))
print("Error as percentage of precise value: " + str(math.fabs((true - _numint2.simpint(fn7, a, b, 7))/_numint2.simpint(fn7, a, b, 7))) + "%")
print

# ANALYSIS AND FINAL COMMENTS
# It seems that, for n = 4, the numerical algorithm yields the exact result (makes sense since the equation is of the fifth order, thus
# the derivative is of the fourth order) and the fit of the approximation would be perfect. Interesting but unsurprising, if we increase n
# after the degree of the equation, a slight error appears since it wouldn't be a perfect match anymore (although still very small).
# Let's compare it to the trapezoidal method:


def f(x):
    return (x + 2. / x) ** 2

a = 1
b = 2
true = 25 / 3

# Vectors
fn1 = (f(a+0*(b-a)/1), f(a+1*(b-a)/1))
fn2 = (f(a+0*(b-a)/2), f(a+1*(b-a)/2), f(a+2*(b-a)/2))
fn3 = (f(a+0*(b-a)/3), f(a+1*(b-a)/3), f(a+2*(b-a)/3), f(a+3*(b-a)/3))
fn4 = (f(a+0*(b-a)/4), f(a+1*(b-a)/4), f(a+2*(b-a)/4), f(a+3*(b-a)/4), f(a+4*(b-a)/4))
fn5 = (f(a+0*(b-a)/5), f(a+1*(b-a)/5), f(a+2*(b-a)/5), f(a+3*(b-a)/5), f(a+4*(b-a)/5), f(a+5*(b-a)/5))

print("For n = 4:")
print(_numint2.simpint(fn4, a, b, 4))
print("Error as percentage of precise value: " + str(math.fabs((true - _numint2.simpint(fn4, a, b, 4))/_numint2.simpint(fn4, a, b, 4))) + "%")
print
print("For n = 5:")
print(_numint2.simpint(fn5, a, b, 5))
print("Error as percentage of precise value: " + str(math.fabs((true - _numint2.simpint(fn5, a, b, 5))/_numint2.simpint(fn5, a, b, 5))) + "%")
print

# We can see that for n = 4, the error in the Simpson's method is one magnitude lower than the trapezoidal method.
# Trapezoidal: 0.0055%; Simpson's: 0.0002%

# One final comment: The equation that provide the maximum error for both methods requires higher-order derivatives of the equation.
# If the equation is not derivable (non-continuous) in the considered interval, the formula can't be used analytically.
