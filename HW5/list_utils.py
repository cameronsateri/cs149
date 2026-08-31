"""Homework 5.1.

Your CS 149 professor has a problem.
They are planning to transfer student grade
data from an old system to a new system, and
they want some changes made to the data.

Author: Cameron Sateri
Version: 10/9/22

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


def move_min_to_front(list):
    """Moves the smallest number in the list to the front.

    Args:
        list (list): a list of grades to be altered.

    Returns:
        sl: sorted list with the smallest number in the front.

    """
    sl = list.copy()
    ln = sl[0]
    for x in list:
        if x < ln:
            ln = x
    sl.remove(ln)
    sl.insert(0, ln)
    return sl
