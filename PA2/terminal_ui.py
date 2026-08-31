""".

Author: Cameron Sateri
Version: 11/21/22
Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


def prompt_for_string(message, minn):
    """Prompts for string to be a certain length.

    Args:
        message (str): string that must be specific length.
        minn (int): minimum length of message.

    Returns:
        test: string that is the correct length based on minn.
    """
    test = ""
    while len(test) < minn:
        test = input(f'{message}: ')
    return test


def prompt_for_int(message, maxx):
    """Prompts for int to be within certain range.

    Args:
        message (str): prompt for inputing int.
        maxx (int): maximum value of inputing.

    Returns:
        val: value within 1 - maxx.
    """
    val = int(input(message + ": "))
    while val < 1 or val > maxx:
        val = int(input(message + ": "))
    return val


def prompt_n_display_hints(solution):
    """Prompts for value to be within certain range.

    Args:
        solution (str): word that will be given hints for.

    """
    test = "f"
    while test == "f" or test == "s" or test == "w":
        print("Want a hint? Enter")
        print("\"f\" for first letter")
        print("\"s\" for first slice")
        print("\"w\" for whole word")
        test = input("\"n\" for none: ")
        if test == "f":
            print(solution[0:1])
        elif test == "s":
            print(solution[0:4])
        elif test == "w":
            print(solution)
