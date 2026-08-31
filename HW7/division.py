"""Homework 7.2.

This code allows the computer to learn the division algorithm.

Author: Cameron Sateri
Version: 10/24/22

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


def divide(num, divisor):
    """Performs the division algorithm to find number/divisor.

    Args:
        num (int): value representing number to be divided.
        divisor (int): value representing the value to be divided by.

    Returns:
        ret (tupple): contains the quotient and the remanider.
    """
    q = 0
    r = num
    while r >= divisor:
        q += 1
        r -= divisor
    ret = (q, r)
    return ret
