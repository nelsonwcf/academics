
'''
module: _optim_u2.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapters on Optimization, the unconstrained case
- implemented from algorithms/pseudocode provided
'''

import random
import _roots

def parabolic(f, x0, x1, x2, es100, imax=1000, ismax=True, debug=False, tab=10, prec=6):
    "locates optimum (maximum if ismax is True, else minimum)"
    #f: function f(x)
    #x0,x2: lower,upper x brackets
    #x1: midpoint (optimum estimate)
    #es100: error tolerance in percentage (0-100)
    #imax: max # of iterations
    #ismax: locate maximum if True, else locate minimum
    #debug: display stats for each iteration
    #tab: tabulated output (0: disable, n: spaces per tab)
    #prec: precision (number of significant digits)
    x0 = float(x0)
    x1 = float(x1)
    x2 = float(x2)
    iter = 1
    ea = 1.
    if debug and tab:
        print("{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}"
              .format("iter","x0","f(x0)","x1","f(x1)","x2","f(x2)","xopt","f(xopt)",t=tab))
    while ea*100 > es100 and iter < imax:
        f0 = f(x0)
        f1 = f(x1)
        f2 = f(x2)
        xopt = (f0*(x1**2-x2**2) + f1*(x2**2-x0**2) + f2*(x0**2-x1**2)) \
             / (2*(f0*(x1-x2) + f1*(x2-x0) + f2*(x0-x1)))
        fopt = f(xopt)
        if debug:
            print(("{:<{t}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}" if tab else
                   "iter={}, x0={:.{p}}, f(x0)={:.{p}}, x1={:.{p}}, f(x1)={:.{p}}, x2={:.{p}}, f(x2)={:.{p}}, xopt={:.{p}}, f(xopt)={:.{p}}")
                  .format(iter, x0, f0, x1, f1, x2, f2, xopt, fopt, t=tab, p=prec))
        if xopt: ea = abs(1 - x1/xopt)
        if (ismax and xopt < x1) or (not ismax and x1 < xopt):
            x2 = x1
        else:
            x0 = x1
        x1 = xopt
        iter += 1
    #end while
    return xopt
#end parabolic()

def newton(df, df2, x0, es100, imax=1000, tv=0, debug=False, tab=10):
    "locates optimum (maximum or minimum)"
    #df: f'(x) = 1st derivative of f(x)
    #df2: f''(x) = 2nd derivative of f(x)
    #x0: initial guess of x
    #es100: error tolerance in percentage (0-100)
    #imax: max # of iterations
    #tv: true value of root
    #debug: display stats for each iteration
    #tab: tabulated output (0: disable, n: spaces per tab)
    return _roots.newton(df, df2, x0, es100, imax, tv, debug, tab)
#end newton()
