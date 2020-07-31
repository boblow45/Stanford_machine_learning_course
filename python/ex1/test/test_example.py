#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import numpy as np
import pytest


from ex1.GradientDescent import compute_cost, gradient_descent, normal_equation


def test_compute_cost():
    expected_cost = 32.07

    # read in the training data from a file
    file = os.path.join(os.path.dirname(__file__), "ex1data1.txt")
    data = np.genfromtxt(file, delimiter=",", dtype=None)

    # break out data in file into features and results
    x, y = data.transpose()

    # put data into the same format, colume vector or matrix
    x = x.reshape((-1, 1))
    y = y.reshape((-1, 1))
    theta = np.zeros((2, 1))

    # add extra column of ones to make gradient descent easier
    x = np.append(np.ones((y.size, 1)), x, axis=1)

    # compute the cost function
    cost = compute_cost(x, y, theta)
    assert expected_cost == pytest.approx(cost, 0.01)


def test_sing_var_gra_descent():
    alpha = 0.01
    iterations = 1500
    expected_theta = np.asarray([[-3.6303], [1.1664]])

    file = os.path.join(os.path.dirname(__file__), "ex1data1.txt")
    data = np.genfromtxt(file, delimiter=",", dtype=None)
    x, y = data[:, 0:-1], data[:, -1]
    y = y.reshape((-1, 1))
    theta = np.zeros((2, 1))

    x = np.append(np.ones((y.size, 1)), x, axis=1)

    calculated_theta = gradient_descent(x, y, theta, alpha, iterations)
    assert expected_theta == pytest.approx(calculated_theta, 0.001)


def test_normal_equation():
    expected_val = np.asarray([[89597.909544], [139.210674], [-8738.019113]])

    file = os.path.join(os.path.dirname(__file__), "ex1data2.txt")
    data = np.genfromtxt(file, delimiter=",", dtype=None)

    x, y = data[:, 0:-1], data[:, -1]
    y = y.reshape((-1, 1))

    x = np.append(np.ones((y.size, 1)), x, axis=1)
    calculated_val = normal_equation(x, y)
    assert expected_val == pytest.approx(calculated_val, 0.001)
