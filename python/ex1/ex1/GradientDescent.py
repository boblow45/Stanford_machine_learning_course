import numpy


def compute_cost(x, y, theta):
    """[summary]

    :param x: [description]
    :type x: numpy.ndarray
    :param y: [description]
    :type y: numpy.ndarray
    :param theta: [description]
    :type theta: numpy.ndarray

    :return: [description]
    :rtype: float
    """

    m = y.size

    weigth = 1 / (2 * m)

    temp = theta.transpose().dot(x.transpose())
    return weigth * numpy.sum(numpy.square(temp.transpose() - y))


def gradient_descent(x, y, theta, alpha, iterations):

    m = y.size
    for ele in range(iterations):
        temp = theta.transpose().dot(x.transpose()).transpose() - y
        theta = theta - (alpha / m * temp.transpose().dot(x).transpose())

    return theta


def normal_equation(x, y):

    return numpy.linalg.inv(x.transpose().dot(x)).dot(x.transpose()).dot(y)
