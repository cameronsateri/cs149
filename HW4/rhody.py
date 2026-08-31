"""Print the song "Go Tell Aunt Rhody.

Author: YOUR NAME HERE
Version: DATE
"""


def print_three_times(phrase):
    """Print the provided phrase three times.

    Args:
        phrase (str): The phrase to print
    """
    print(phrase)
    print(phrase)
    print(phrase)


def print_verse(intro, conclusion):
    """Print one verse of Go Tell Aunt Rhody.

    Args:
        intro (str): First three lines
        conclusion (str): Last line
    """
    print_three_times(intro)
    print(conclusion + "\n")


def print_chorus():
    """Print the chorus of Go Tell Aunt Rhody."""
    print_verse("Go tell Aunt Rhody", "The old gray goose is dead")


def print_aunt_rhody():
    """Print the lyrics to Go Tell Aunt Rhody."""
    print_chorus()
    print_verse("The one she's been saving", "To make a feather bed")
    # UNFINISHED! ADD YOUR CODE HERE.


if __name__ == "__main__":
    print_aunt_rhody()
    print_verse("The goslings are mourning", "Because their mother's dead")
    print_verse("The old gander's weeping", "Because his wife is dead")
    print_verse("She died in the mill pond", "From standing on her head")
    print_chorus()