"""Homework 6.3.

This code is used for playing blackjack.

Author: Cameron Sateri
Version: 10/19/22

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""
# comparison values.
card_tupple = ('0', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10')
royal_cards = ('J', 'Q', 'K')


def get_value(cv):
    """Returns int value of card.

    Args:
        cv (string): string of the card.

    Returns:
        int: integer value representing card value.
    """
    if cv in royal_cards:
        return 10
    if cv == card_tupple[1]:
        return 1
    for x in range(11):
        if cv == card_tupple[x]:
            return x


def dealer_hits(card1, card2):
    """Returns true or false based on if the dealer should or shouldnt hit.

    Args:
        card1 (string): first card value.
        card2 (string): second card value.

    Returns:
        boolean: true if should hit, false if should not.
    """
    if get_value(card1) == 1 and card2 in royal_cards:
        return False
    if get_value(card2) == 1 and card1 in royal_cards:
        return False
    elif get_value(card1) + get_value(card2) < 17:
        return True
    else:
        return False
