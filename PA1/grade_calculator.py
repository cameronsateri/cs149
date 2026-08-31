"""PA 2.

.

Author: Cameron Sateri
Version: 11/2/22

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


def average(flt):
    """Determines averages between a classes scores.

    Args:
        flt (list): list of floats.

    Returns:
        av (float): average scores.

    """
    score = 0
    count = 0
    for x in flt:
        if x != -1.0:
            score += x
            count += 1
    return (score / count)


def grade_totals(tup):
    """Creates a dictionary from a list of tupples representing assignments.

    Args:
        tup (list): list of tupples.

    Returns:
        grades (dictionary): dictionary of grades.

    """
    grades = {}
    for x in range(len(tup)):
        grades[tup[x][0]] = 0
    for x in range(len(tup)):
        grades[tup[x][0]] += tup[x][1]
    return grades
