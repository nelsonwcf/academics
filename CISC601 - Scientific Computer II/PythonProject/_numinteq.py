
'''
module: _numinteq.py
author: Luis Paris
description:
- formulas from Chapra's numerical methods textbook
- chapters on numeric integration for continuous functions
- implemented from algorithms/pseudocode provided
'''

import sys  #for debug output finer control
import numpy as np

def trapeq(f, x0, xn, n):
    h = (xn - x0) / float(n)
    x = x0
    sum = f(x)
    for i in range(1, n):
        x += h
        sum += 2*f(x)
    sum += f(xn)
    return h * sum / 2.
#end trapeq()

def romberg(f, x0, xn, es100=.5, imax=1000, tv=0, debug=False, precision=6, tab=12):
    I = np.zeros((10,10))
    I[0,0] = trapeq(f, x0, xn, n=1)
    ea = 1.
    iter = 0
    while ea*100 >= es100 and iter < imax:
        iter += 1
        I[iter,0] = trapeq(f, x0, xn, n=2**iter)
        for k in range(1, iter+1):
            j = iter - k
            I[j,k] = (4**k * I[j+1,k-1] - I[j,k-1]) / (4**k - 1)
        ea = abs(1 - I[1,iter-1] / I[0,iter])
    #end while
    if debug:
        sys.stdout.write('{:<{t}}'.format('iter:', t=tab))
        for i in range(1, iter+2): sys.stdout.write('{:<{t}}'.format(i, t=tab))
        sys.stdout.write('\n')
        if tv:
            sys.stdout.write('{:<{t}}'.format('et:', t=tab))
            for i in range(iter+1):
                sys.stdout.write('{:<{t}.{p}%}'.format(abs(1 - I[0,i] / tv), t=tab, p=precision))
            sys.stdout.write('\n')
        sys.stdout.write('{:<{t}}{:<{t}}'.format('ea:', '', t=tab))
        for i in range(1,iter+1):
            sys.stdout.write('{:<{t}.{p}%}'.format(abs(1 - I[1,i-1] / I[0,i]), t=tab, p=precision))
        for i in range(iter+1):
            sys.stdout.write('\n{:<{t}}'.format('n=' + str(1<<i) + ':', t=tab))
            for j in range(iter+1 - i):
                sys.stdout.write('{:<{t}.{p}f}'.format(I[i,j], t=tab, p=precision))
        sys.stdout.write('\n')
    #end if debug
    return I[0,iter]
#end romberg()

def E_romberg(I1, h1, I2, h2): return (I1 - I2) / (1 - (h1/float(h2))**2)
