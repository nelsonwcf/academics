
'''
module: _ode2.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapters on ordinary differential equations (ODEs)
- implemented from algorithms/pseudocode provided
comments:
- the following ODE algorithms implement ONE iteration to estimate the next value of y, given:
  * reference points x,y
  * df(x,y)/dx (or estimate) at reference points x,y
'''

def heuniter(dfxy, x, y, h, es100=1.0, imax=20, debug=False):
    d1 = dfxy(x, y)
    ye = y + d1*h
    iter = 0; ea = 1.0
    while True:
        if debug: print("  iter={}, ye={}, ea={:%}".format(iter, ye, ea))
        if es100 >= abs(ea*100) or iter >= imax:
            break
        d2 = dfxy(x+h, ye)
        m = (d1 + d2) / 2.0
        ye0 = ye
        ye = y + m*h
        ea = 1 - ye0/ye
        iter += 1
    #end while
    return ye
#end heun()

def RK2(dfxy, x, y, h, a2):
    a1 = 1 - a2
    p1 = q11 = 1/(2.*a2)
    k1 = dfxy(x, y)
    k2 = dfxy(x + p1*h, y + q11*k1*h)
    return y + (a1*k1 + a2*k2)*h
#end RK2()

def ralston(dfxy, x, y, h):
    return RK2(dfxy, x, y, h, a2=2/3.0)
#end ralston()
