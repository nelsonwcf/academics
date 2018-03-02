
'''
module: _optim_u.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapters on Optimization, the unconstrained case
- implemented from algorithms/pseudocode provided
'''

import math

#Golden-section search for the optimum (maximum or minimum)
def gold(f, xl, xu, es100, imax=1000, ismax=True, debug=False, tab=10, prec=6):
    "locates optimum (maximum if ismax is True, else minimum)"
    #f: function f(x)
    #xl,xu: lower,upper x brackets
    #es100: error tolerance in percentage (0-100)
    #imax: max # of iterations
    #ismax: locate maximum if True, else locate minimum
    #debug: display stats for each iteration
    #tab: tabulated output (0: disable, n: spaces per tab)
    #prec: precision (number of significant digits)
    xl = float(xl)
    xu = float(xu)
    R = (math.sqrt(5) - 1) / 2.
    d = R * (xu - xl)
    x1 = xl + d
    x2 = xu - d
    f1 = f(x1)
    f2 = f(x2)
    iter = 1
    ea = 1.
    if debug and tab:
        print("{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}{:<{t}}"
              .format("iter","xl","f(xl)","x2","f(x2)","x1","f(x1)","xu","f(xu)","d",t=tab))
    while ea*100 > es100 and iter < imax:
        if debug:
            print(("{:<{t}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}{:<{t}.{p}}" if tab else
                   "iter={}, xl={:.{p}}, f(xl)={:.{p}}, x2={:.{p}}, f(x2)={:.{p}}, x1={:.{p}}, f(x1)={:.{p}}, xu={:.{p}}, f(xu)={:.{p}}, d={:.{p}}")
                  .format(iter,xl,f(xl),x2,f2,x1,f1,xu,f(xu),d,t=tab,p=prec))
        d = R * d; xint = xu - xl
        if (ismax and f1 > f2) or (not ismax and f1 < f2):
            xopt = x1
            fx = f1
            xl = x2
            x2 = x1
            x1 = xl + d
            f2 = f1
            f1 = f(x1)
        else:
            xopt = x2
            fx = f2
            xu = x1
            x1 = x2
            x2 = xu - d
            f1 = f2
            f2 = f(x2)
        if xopt != 0:
            ea = (1 - R) * abs(xint / xopt)
        iter += 1
    #end while
    return xopt
#end gold()
