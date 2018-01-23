"""
This file contains tests 
"""
import numpy as np
from integrate.newton_cotes import simpson
from integrate.newton_cotes import trapz
import pytest

def f(x):
    return np.power(x, 2)

def g(x):
    return 3 * x

def test_simpson():
    x = np.array([0, 3])
    I = simpson.evaluate(x, f)
    assert I == 9.0

def test_trapz():
    x = np.array([0, 10])
    I = trapz.evaluate(x, g)
    assert I ==  150.0
