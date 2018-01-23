"""
This module implements 1d and 2d Monte Carlo integration
"""

import numpy as np

def monte_1d(x, f, trials):
   a = x[0]
   b = x[1]
   d = (b - a) *  np.random.rand(1, trials) + a
   y = f(d)
   return (b-a) * np.sum(y) / trials

def monte_2d(f, v, domain, trials):
    area = np.prod(domain[1] - domain[0])
    matrix = np.sqrt(area) * np.random.rand(trials, 2) + np.min(domain)
    v_eval = v(matrix) 
    idx = np.where(v_eval < 1.0)
    points_inside = v_eval[idx]
    k = points_inside.size
    return area * k / trials
