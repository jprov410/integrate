"""
This file contains the implementation of the trapezoidal rule
"""

import numpy as np

def evaluate(x, f):
    a = x[0]
    b = x[1]
    ya = f(a)
    yb = f(b)
    I = (b-a) * (ya + yb) / 2
    return I

