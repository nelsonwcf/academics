from __future__ import division
import _numinteq
import _numint
import math
import _plot

print("Exercise 23.1")
print("------------------")


def f(x):
    return math.cos(x)


def f2(x):
    return -math.sin(x)

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


def f2ch2(x, h):
    return (f(x+h) - 2*f(x) + f(x-h)) / (h**2)


def f2ch4(x, h):
    return (-f(x+2*h) + 16*f(x+h) -30*f(x) + 16*f(x-h) - f(x-2*h)) / (12 * h ** 2)


def foh(x, h):
    return tv-ffh(x, h)


def foh2(x, h):
    return tv-ffh2(x, h)


def boh(x, h):
    return tv-fbh(x, h)


def boh2(x, h):
        return tv-fbh2(x, h)


def coh2(x, h):
    return tv-fch2(x, h)


def coh4(x, h):
    return tv-fch4(x, h)


print "First-derivative forward"
print "----"
print("f'(x) on O(h): " + str(round(ffh(c,h),5)))
print("O(h):" + str(round(foh(c, h),5)))
print("e(t): " + str(100 * abs(round((ffh(c,h)-tv)/tv,5))) + "%")
print
print("f'(x) on O(h^2): " + str(round(ffh2(c,h),5)))
print("O(h^2):" + str(round(foh2(c, h),5)))
print("e(t): " + str(100 * abs(round((ffh2(c,h)-tv)/tv,5))) + "%")
print

print "First-derivative backward"
print "----"
print("f'(x) on O(h): " + str(round(fbh(c,h),5)))
print("O(h):" + str(round(boh(c, h),5)))
print("e(t): " + str(100 * abs(round((fbh(c,h)-tv)/tv,5))) + "%")
print
print("f'(x) on O(h^2): " + str(round(fbh2(c,h),5)))
print("O(h^2):" + str(round(boh2(c, h),5)))
print("e(t): " + str(100 * abs(round((fbh2(c,h)-tv)/tv,5))) + "%")
print

print "First-derivative centered"
print "----"
print("f'(x) on O(h^2): " + str(round(fch2(c,h),5)))
print("O(h^2):" + str(round(coh2(c, h),5)))
print("e(t): " + str(100 * abs(round((fch2(c,h)-tv)/tv,5))) + "%")
print
print("f'(x) on O(h^4): " + str(round(fch4(c,h),5)))
print("O(h^4):" + str(round(coh4(c, h),5)))
print("e(t): " + str(100 * abs(round((fch4(c,h)-tv)/tv,5))) + "%")
print
print("Analysis:")
print("As mentioned by the author, the addition of another term from Taylor series reduced the error by more")
print("than one magnitude in the forward and backward finite-divided-difference (fdds) formulas. On the centered")
print("version, the error was reduced from O(h^2) to O(h^4), which means that by dividing the step by half would")
print("reduce the error by 1/8. I believe the main point of this exercise is to show that by using Taylor, it is")
print("possible to significantly improving the precision by just adding another term to the series. The important")
print("of this method becomes more evident when used to estimate derivatives of higher orders.")
print
print


print("Exercise 23.2")
print("------------------")


def f(x):
    return math.log(x, math.e)


def f2(x):
    return 1/x

c = 25
h = 2
tv = f2(c)
print("True value of f2(xi): " + str(tv))
print("xi: " + str(c))
print("h: " + str(h))
print
print "First-derivative forward"
print "----"
print("f'(x) on O(h): " + str(round(ffh(c,h),5)))
print("O(h):" + str(round(foh(c, h),5)))
print("e(t): " + str(100 * abs(round((ffh(c,h)-tv)/tv,5))) + "%")
print
print("f'(x) on O(h^2): " + str(round(ffh2(c,h),5)))
print("O(h^2):" + str(round(foh2(c, h),5)))
print("e(t): " + str(100 * abs(round((ffh2(c,h)-tv)/tv,5))) + "%")
print

print "First-derivative backward"
print "----"
print("f'(x) on O(h): " + str(round(fbh(c,h),5)))
print ("O(h):" + str(round(boh(c, h),5)))
print("e(t): " + str(100 * abs(round((fbh(c,h)-tv)/tv,5))) + "%")
print
print("f'(x) on O(h^2): " + str(round(fbh2(c,h),5)))
print ("O(h^2):" + str(round(boh2(c, h),5)))
print("e(t): " + str(100 * abs(round((fbh2(c,h)-tv)/tv,5))) + "%")
print

print "First-derivative centered"
print "----"
print("f'(x) on O(h^2): " + str(round(fch2(c,h),5)))
print ("O(h^2):" + str(round(coh2(c, h),5)))
print("e(t): " + str(100 * abs(round((fch2(c,h)-tv)/tv,5))) + "%")
print
print("f'(x) on O(h^4): " + str(round(fch4(c,h),5)))
print ("O(h^4):" + str(round(coh4(c, h),5)))
print("e(t): " + str(100 * abs(round((fch4(c,h)-tv)/tv,5))) + "%")
print
print("Analysis:")
print("This exercise is similar to the previous one and carry the same conclusions.")
print
print
print("Exercise 23.3")
print("NOTE: I'm doing this third exercise to test ffds approach for derivatives of higher orders, which wasn't done")
print("in the first two exercises")
print("------------------")
print


def f(x):
    return math.e**x


def f2(x):
    return math.e**x


def f3(x):
    return math.e**x

c = 2
h = 0.1
d2tv = f2(c)
d3tv = f3(c)
print("True value of f2(xi): " + str(d2tv))
print("True value of f3(xi): " + str(d3tv))
print("xi: " + str(c))
print("h: " + str(h))

print "First-derivative centered"
print "----"
print("f'(x) on O(h^2): " + str(round(fch2(c,h),5)))
print("e(t): " + str(100 * abs(round((fch2(c,h)-d2tv)/d2tv,5))) + "%")
print
print("f'(x) on O(h^4): " + str(round(fch4(c,h),5)))
print("e(t): " + str(100 * abs(round((fch4(c,h)-d2tv)/d2tv,5))) + "%")
print
print "Second-derivative centered"
print "----"
print("f''(x) on O(h^2): " + str(round(f2ch2(c,h),5)))
print("e(t): " + str(100 * abs(round((f2ch2(c,h)-d3tv)/d3tv,5))) + "%")
print
print("f''(x) on O(h^4): " + str(round(f2ch4(c,h),5)))
print("e(t): " + str(100 * abs(round((f2ch4(c,h)-d3tv)/d3tv,5))) + "%")
print
print("Analysis:")
print("This exercise had the characteristic that the derivative of the exponential function of x is the same as the")
print("original function. Thus, it became more of a comparison between the methods for the same function. One noticeable")
print("thing is that the error of the O(h^2) and O(h^4) functions for the second derivative are half of those on the first")
print("derivative. This would be expected since we more terms from the series usually leads to more precision.")


