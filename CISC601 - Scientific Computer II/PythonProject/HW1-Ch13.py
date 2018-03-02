import _optim_u
import _optim_u2
import math
import _plot
import _roots

print("Exercise 13.6");
print

def f(x):
    return (4 * x - 1.8 * x ** 2 + 1.2 * x ** 3 - 0.3 * x ** 4);

xl = -2;
xu = 4;
e = 0.01;

# _plot.graph(f, xl, xu);
# By the plot, we can visually see the max being between 2 and 3.

# a)
xopt = _optim_u.gold(f, xl, xu, es100=e);
print "a)", xopt;

# b)
x0 = 1.75;
x1 = 2;
x2 = 2.5;
iter = 10;
xopt = _optim_u2.parabolic(f, x0, x1, x2, imax = 100, es100 = e);
print "b)", xopt;

# c)
x0 = 3;
e = 0.01;

def df(x):
    return (4 - 3.6 * x + 3.6 * x ** 2 - 1.2 * x ** 3);
def df2(x):
    return (-3.6 + 7.2 * x - 3.6 * x ** 2);

xopt = _optim_u2.newton(df, df2, x0, es100=e);
print "c)",xopt;
print

print "Exercise 13.10"
print

def f(x):
    return (-(3 + 6 * x + 5 * x ** 2 + 3 * x ** 3 + 4 * x ** 4));

def df(x):
    return (6 + 10 * x + 9 * x ** 2 + 16 * x ** 3);

xl = -2;
xu = 1;
e = 0.01;

#_plot.graph(f, xl, xu);

xopt = _roots.bisect(df, xl, xu, es100 = e);
print "Using bisect method on dif f: ", xopt
xopt = _optim_u.gold(f, xl, xu, es100=e);
print "Using gold method on -f: ", xopt
