
'''
module: _ode.py
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

def euler(dfxy, x, y, h):
    return y + dfxy(x, y) * h
#end euler()

def heun(dfxy, x, y, h):
    d1 = dfxy(x, y)
    y1 = y + d1*h
    d2 = dfxy(x+h, y1)
    m = (d1 + d2) / 2.0
    return y + m*h
#end heun

def midpoint(dfxy, x, y, h):
    dy = dfxy(x, y)
    ym = y + dy*h/2
    m = dfxy(x+h/2, ym)
    return y + m*h
#end midpoint()
