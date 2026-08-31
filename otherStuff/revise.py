"""Lab 14.

This file is for practicing coditional statements and loops.

Author: Cameron Sateri
Version: 11/8/22

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


def calculate_success(ambition, skill, effort):
    """Calculates how successful one is to be.

    Args:
        ambition (boolean): if one has ambition or not.
        skill (boolean): if one has skill or not.
        effort (boolean): if one has effort or not.

    Returns:
        scs (int): percent based on how successful one will be.
    """
    if ambition and skill and effort:
        return 100
    elif ambition and skill:
        return 65
    elif ambition and effort:
        return 60
    elif skill and effort:
        return 70
    elif ambition or skill or effort:
        return "It’s a challenge but we can still make it!"
    else:
        return 0


def reverse_usingFor(string):
    """Reverses the contents of a string using a for loop.

    Args:
        string (str): strait forward version of string.

    Returns:
        ret (str): reversed version of the string.
    """
    ret = []
    for x in range((len(string) -1) , -1 , -1):
        ret.append(string[x])
    return ret


def reverse_usingWhile(string):
    """Reverses the contents of a string using a while loop.

    Args:
        string (str): strait forward version of string.

    Returns:
        ret (str): reversed version of the string.
    """
    ret = ""
    x = len(string) - 1
    while x >= 0:
        if string[x] == "a" or string[x] == "e":
            ret += ""
        else:
            ret += string[x]
        x -= 1
    return ret
