import numpy as np


def sphere_model(x):
    cost = sum(x**2)
    return cost


def schweifel_problem_1(x):
    cost = sum(abs(x)) + np.product(abs(x))
    return cost
