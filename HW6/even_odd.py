"""Homework 6.1.

This determiens even numbers from odd numbers and sorts them into the
accompanying list.

Author: Cameron Sateri
Version: 10/11/22

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


def sort_even_and_odd(number, evens, odds):
    """Append the provided number to the correct list.

    If the number is even, append it to evens, if it is odd append it to odds.
    Print the error message 'Rejected float' if the number is a float.

    Args:
        number (int): the number to sort
        evens (list): destination list for even numbers
        odds (list): destination list for odd numbers

    """
    if type(number) == float:
        print("Rejected float")
    elif number % 2 == 0:
        evens.append(number)
    elif number % 2 == 1:
        odds.append(number)


if __name__ == '__main__':
    # an example of how this function might be used.
    evens = []
    odds = []

    sort_even_and_odd(4, evens, odds)
    sort_even_and_odd(16, evens, odds)
    sort_even_and_odd(-5, evens, odds)
    sort_even_and_odd(100, evens, odds)
    sort_even_and_odd(7, evens, odds)
    sort_even_and_odd(2.5, evens, odds)  # Should print 'Rejected float'

    print(f"evens: {evens}")  # Should print 'evens: [4, 16, 100]'
    print(f"odds: {odds}")  # Should print 'odds: [-5, 7]'
