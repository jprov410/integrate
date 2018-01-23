"""
This file contains the implementation of the Simpson rule
"""

import numpy as np

def evaluate(bounds , func):
    """

    Evaluates simpsons rules on an array of values and a funtion pointer

    .. math::
          
        \int_{a}^{b} = \sum_i ...

    parameters
    ----------
    bounds : array_like
        An array with dimension of 2 that contains the integration bounds
    func : function
        integrand to be evaluated

    returns
    -------
    integral : float
        The integral of the function on the domain specified by bounds

    """
    if len(bounds) != 2:
        raise ValueError("Bounds should contain 2 elements, found %d." % len(bounds))

    a = bounds[0]
    b = bounds[1]
    ya = func(a)
    yb = func((a+b)/2.)
    yc = func(b)
    I = (b-a) * (ya + 4. * yb + yc) / 6.
    return I

