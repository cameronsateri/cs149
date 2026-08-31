""".

Author: Cameron Sateri
Version: 11/21/22
Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


def word_splicer(solutions):
    """Splits words in half.

    Args:
        solutions (list): list of words to be split in half.

    Returns:
        fixed: list of words having been spliced in two.
    """
    fixed = []
    for x in solutions:
        fixed.append(x[:len(x)//2])
        fixed.append(x[len(x)//2:])
    return fixed


def clue_to_string(clues):
    """Creates list of clues in a numbered format.

    Args:
        clues (list): list of strings to be counted to numbered list.

    Returns:
        string: string with all of the lists from clues.
    """
    string = ""
    for x in clues:
        string += str(clues.index(x) + 1) + ") " + x
        string += "\n"
    return string


def board_to_string(board):
    """Turns strings into organized list.

    Args:
        board (list): list of words to be sorted.

    Returns:
        message: string that has been correctly lengthed.
    """
    string = ""
    for x in board:
        length = 9 + len(x)
        string += "-" * length
        string += "\n"
        string += "| " + "{:02d}".format(board.index(x) + 1) + " | " + x + " |"
        string += "\n"
        string += "-" * length
        string += "\n"
    return string
