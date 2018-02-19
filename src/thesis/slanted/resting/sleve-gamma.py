#!/usr/bin/python3
import math
import numpy as np

def h_max(h):
    m = None
    for x in np.linspace(-25e3, 25e3, 1000):
        if m is None:
            m = h(x)
        elif h(x) > m:
            m = h(x)

    return m

def gamma(h1, h2, H, s1, s2):
    return 1 - h_max(h1) / s1 * math.cosh(H/s1)/math.sinh(H/s1) - \
            h_max(h2) / s2 * math.cosh(H/s2)/math.sinh(H/s2)

s1 = 8e3
s2 = 6e3
H = 20e3

h0 = 6e3
a = 5e3
lmbda = 4e3

h = lambda x: h0*math.exp(-(x/a)**2) * math.cos(math.pi*x/lmbda)**2
h1 = lambda x: 0.5 * h0 * math.exp(-(x/a)**2)
h2 = lambda x: h(x) - h1(x)

print(gamma(h1, h2, H, s1, s2))
