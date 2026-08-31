"""Lab 13.

.

Author: Cameron Sateri
Version: 10/21/22

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
from pysyllables import get_syllable_count


def check_n_syllables(lst, nos):
    """Compares number of syllables to given value, returns >, <, or =.

    Args:
        lst (list): list of words on a line.
        nos (int): number of syllables to validate.

    Returns:
        -1, 0, or 1 (int): determines if there are less (-1), equal (0),
        or more (1) syllables in a given word.
    """
    syl = 0
    for x in lst:
        syl += get_syllable_count(x)
    if nos < syl:
        return -1
    elif nos > syl:
        return 1
    else:
        return 0


def validate_haiku(lst):
    """Determines the validity of a haiku.

    Args:
        lst (list): list of lines (also lists) in a haiku.

    Returns:
        eror (string): string of errors if there are any.
    """
    # empty return statement.
    eror = ""
    # determines if list is 3 lines or not.
    if len(lst) != 3:
        return "Invalid haiku, not 3 lines."
    # determines errors in line 1.
    if check_n_syllables(lst[0], 5) == 1:
        eror = eror + "Line 1 too long. "
    elif check_n_syllables(lst[0], 5) == -1:
        eror = eror + "Line 1 too short. "
    # determines errors in line 2.
    if check_n_syllables(lst[1], 7) == 1:
        eror = eror + "Line 2 too long. "
    elif check_n_syllables(lst[1], 7) == -1:
        eror = eror + "Line 2 too short. "
    # determines errors in line 3.
    if check_n_syllables(lst[2], 5) == 1:
        eror = eror + "Line 3 too long. "
    elif check_n_syllables(lst[0], 5) == -1:
        eror = eror + "Line 3 too short. "
    # determines if there are errors and returns them if so.
    if len(eror) == 0:
        return "Valid haiku"
    else:
        return eror
