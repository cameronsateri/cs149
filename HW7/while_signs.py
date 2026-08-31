"""Homework 7.1.

This code sorts any amount of positive and negative numbers.

Author: Cameron Sateri
Version: 10/24/22

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


def get_positive_negative():
    """Sorts any amount of positive and negative numbers.

    Returns:
        ret (tupple): two lists containing positive then negative values.
    """
    p = []
    n = []
    x = 0
    while x == 0:
        num = input("Input? ")
        if num == "q":
            x = 1
            break
        num = float(num)
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
    ret = (p, n)
    return ret
