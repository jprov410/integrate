"""
Testing the integrate package
"""

import integrate
import pytest
import numpy as np

def g(x):
    return 3.0 * x

def f(x):
    return np.power(x, 2)

def h(x):
    return np.ones(x.size)

def volume(x):
    squares = np.power(x, 2)
    return np.sum(squares, axis=1)

def test_trapz():
    x = np.array([0, 10])
    I = integrate.newton_cotes.trapz.evaluate(x, g)
    assert I == 150.00

def test_simpson():
    x = np.array([0, 3])
    I = integrate.newton_cotes.simpson.evaluate(x, f)
    assert I == 9.00

def test_monte1d():
    x = np.array([0, 3])
    I = integrate.stochastic.monte_carlo.monte_1d(x, f, 100000)
    assert np.allclose(I, 9.00, 1e-2)

def test_monte2d():
    domain = np.array([[-1, -1], [1, 1]])
    I = integrate.stochastic.monte_carlo.monte_2d(h, volume, domain, 1000000)
    assert np.allclose(I, np.pi, 1e-2)
