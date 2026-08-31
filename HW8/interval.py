"""Homework 8.1.

This code sorts numbers based on a certain interval.

Author: Cameron Sateri
Version: 10/28/22

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


def in_interval(fl, lb, ub, ci=True):
    """Returns numbers within the interval in list fl.

    Args:
        fl (list): list of floats.
        lb (int): lower bound of the interval.
        ub (int): upper bound of the interval.
        ci (boolean): indicator whether this is a closed interval.

    Returns:
        ret (list): list containing numbers in interval.
    """
    ret = []
    for x in fl:
        if x <= ub and x >= lb and ci:
            ret.append(x)
        elif x < ub and x > lb:
            ret.append(x)
    return ret
