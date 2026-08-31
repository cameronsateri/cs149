import math


def sphere_volume(radius):
    return (4/3.0) * math.pi * pow(radius, 3)


def normal_pdf(mu, sigma, x):
    ret = (1 / (sigma * pow(2 * math.pi, 1/2)))
    a = -1 * pow(x - mu, 2)
    b = 2 * pow(sigma, 2)
    ret = ret * pow(math.e, a / b)
    return ret
