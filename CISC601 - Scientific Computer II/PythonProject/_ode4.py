
'''
module: _ode4.py
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

def RK5kc(dfxy, x, y, h):
    def a(i): return {2:1./5, 3:3./10, 4:3./5, 5:1., 6:7./8}[i]
    def b(i): return {21:1./5, 31:3./40, 32:9./40, 41:3./10, 42:-9./10, 43:6./5,
                      51:-11./54, 52:5./2, 53:-70./27, 54:35./27, 61:1631./55296,
                      62:175./512, 63:575./13824, 64:44275./110592, 65:253./4096}[i]
    def c(i): return {1:37./378, 3:250./621, 4:125./594, 6:512./1771}[i]
    def dc(i): return {1:c(1)-2825./27648, 3:c(3)-18575./48384, 4:c(4)-13525./55296,
                       5:-277./14336, 6:c(6)-1./4}[i]
    dy = dfxy(x, y)
    ytmp = y + b(21)*h*dy
    k2 = dfxy(x + a(2)*h, ytmp)
    ytmp = y + h*(b(31)*dy + b(32)*k2)
    k3 = dfxy(x + a(3)*h, ytmp)
    ytmp = y + h*(b(41)*dy + b(42)*k2 + b(43)*k3)
    k4 = dfxy(x + a(4)*h, ytmp)
    ytmp = y + h*(b(51)*dy + b(52)*k2 + b(53)*k3 + b(54)*k4)
    k5 = dfxy(x + a(5)*h, ytmp)
    ytmp = y + h*(b(61)*dy + b(62)*k2 + b(63)*k3 + b(64)*k4 + b(65)*k5)
    k6 = dfxy(x + a(6)*h, ytmp)
    yout = y + h*(c(1)*dy + c(3)*k3 + c(4)*k4 + c(6)*k6)
    yerr = h*(dc(1)*dy + dc(3)*k3 + dc(4)*k4 + dc(5)*k5 + dc(6)*k6)
    return yout, yerr
#end RK5kc()

def h_adapt(dfxy, x, y, h, yscal, eps, safety=.9, econ=1.89e-4):
    while True:
        ytmp, yerr = RK5kc(dfxy, x, y, h)
        emax = abs(yerr/yscal/eps)
        if emax <= 1:
            break
        htmp = safety*h*emax**-.25
        h = max(abs(htmp), .25*abs(h))
        xnew = x + h
        if xnew == x: pass
    #end while
    hnext = safety*h*emax**-.2 if emax > econ else 4.*h
    return ytmp, hnext/1.5
#end h_adapt()
