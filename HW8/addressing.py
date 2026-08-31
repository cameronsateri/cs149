"""Homework 8.2.

This code returns all possible street addresses on a street.

Author: Cameron Sateri
Version: 10/28/22

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


def generate_addresses(sn, ina, ub, ival):
    """Creates all possible street addresses along an interval.

    Args:
        sn (str): name of the street.
        ina (int): initial numerical address.
        ub (int): upper bound of the numerical address values.
        ival (int): interval between numerical addresses.

    Returns:
        ret (list): list containing all street addresses.
    """
    ret = []
    for x in range(ina, ub, ival):
        ret.append(f'{x} {sn}')
    return ret
