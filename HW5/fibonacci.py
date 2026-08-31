"""Homework 5.2.

Computes the fibonacci sequence

Author: Cameron Sateri
Version: 10/9/22

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


def start_sequence():
    """Returns the first 2 integers in the fibonacci sequence.

    Returns:
        list: list containing the first 2 numebrs of
        the fibonacci sequence.

    """
    list = [1, 1]
    return list


def add_next_number(list):
    """Takes the current list and adds the next number in the fibonacci sequence to it.

    Args:
        list (list): a list of the current sequence.

    """
    list.append(list[-2] + list[-1])
