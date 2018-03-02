
'''
module: _ode3.py
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

def RK4(dfxy, x, y, h):
    k1 = dfxy(x, y)
    ym = y + k1*h/2.
    k2 = dfxy(x + h/2., ym)
    ym = y + k2*h/2.
    k3 = dfxy(x + h/2., ym)
    ye = y + k3*h
    k4 = dfxy(x + h, ye)
    m = (k1 + 2*(k2 + k3) + k4)/6.
    return y + m*h
#end RK4()
