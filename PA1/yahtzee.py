"""
Computes the scores for Yahtzee, a dice game by Milton Bradley.

Author: Cameron Sateri
Version: 11/7/22
Honor Code:
"""

ONES = 1

TWOS = 2

THREES = 3

FOURS = 4

FIVES = 5

SIXES = 6

THREE_OF_A_KIND = 9

FOUR_OF_A_KIND = 10

FULL_HOUSE = 11

SMALL_STRAIGHT = 12

LARGE_STRAIGHT = 13

YAHTZEE = 14

CHANCE = 15


def add_values(dice):
    """Adds the values of the five dice in the list.

    Args:
        dice(list): list of 5 int dice values.

    Returns:
        (int):added value of the dice (index 0 to 4)
    """
    value = 0
    # Write the rest of this function(you do not need to use loops, can just add the
    # the five indexed elements in the dice list.
    for x in dice:
        value += x
    return value


def calculate_score(dice, category):
    """Score calculation for the given turn.

    Args:
        dice(list):list of 5 dice values.
        category(int):category selected by the player

    Returns:
        score(int):number of points, or 0 if N/A
    """
    # Write a decision statement to evaluate the score for each category.
    # Cases that require more than several lines of code should be done
    # in separate methods below. Each case should set the value of the
    # score variable, so that you will have only one return statement.
    score = 0
    if category <= SIXES and category >= ONES:
        score = upper_section(dice, category)
    elif category == THREE_OF_A_KIND:
        score = three_of_a_kind(dice)
    elif category == FOUR_OF_A_KIND:
        score = four_of_a_kind(dice)
    elif category == FULL_HOUSE:
        score = full_house(dice)
    elif category == SMALL_STRAIGHT:
        score = small_strait(dice)
    elif category == LARGE_STRAIGHT:
        score = large_strait(dice)
    elif category == YAHTZEE:
        score = yahtzee(dice)
    elif category == CHANCE:
        score = chance(dice)
    return score


def upper_section(dice, category):
    """Scores points between 1-6.

    Args:
        dice(list):list of 5 dice values.
        category(int):category selected by the player

    Returns:
        score(int):number of points, or 0 if N/A
    """
    score = 0
    for x in dice:
        if x == category:
            score += 1
    score *= category
    return score


def three_of_a_kind(dice):
    """Score calculation based on 3 of a kind.

    Args:
        dice(list):list of 5 dice values.

    Returns:
        score(int):number of points, or 0 if N/A
    """
    for x in dice:
        if dice.count(x) >= 3:
            return add_values(dice)
    return 0


def four_of_a_kind(dice):
    """Score calculation based on 4 of a kind.

    Args:
        dice(list):list of 5 dice values.

    Returns:
        score(int):number of points, or 0 if N/A
    """
    for x in dice:
        if dice.count(x) >= 4:
            return add_values(dice)
    return 0


def full_house(dice):
    """Score calculation determining if its a full house.

    Args:
        dice(list):list of 5 dice values.

    Returns:
        score(int):number of points, or 0 if N/A
    """
    c2 = False
    c3 = False
    for x in dice:
        if dice.count(x) == 2:
            c2 = True
        elif dice.count(x) == 3:
            c3 = True
    if c2 and c3:
        return 25
    return 0


def small_strait(dice):
    """Score calculation determining if there is a small strait.

    Args:
        dice(list):list of 5 dice values.

    Returns:
        score(int):number of points, or 0 if N/A
    """
    score = 1
    dice.sort()
    r = 0
    while r < 4:
        if dice[r] == dice[r + 1] - 1:
            score += 1
        else:
            score = 1
        if score == 4:
            return 30
        r += 1
    for x in range(len(dice) - 1):
        if dice[x] == dice[x + 1] - 1:
            score += 1
        else:
            score = 1
        if score == 4:
            return 30
    return 0


def large_strait(dice):
    """Score calculation determining if there is a large strait.

    Args:
        dice(list):list of 5 dice values.

    Returns:
        score(int):number of points, or 0 if N/A
    """
    score = 1
    dice.sort()
    for x in range(len(dice) - 1):
        if dice[x] == dice[x + 1] - 1:
            score += 1
        else:
            score = 1
        if score == 5:
            return 40
    return 0


def yahtzee(dice):
    """Score calculation seeing if all 5 dice are the same.

    Args:
        dice(list):list of 5 dice values.

    Returns:
        score(int):number of points, or 0 if N/A
    """
    if dice.count(dice[0]) == 5:
        return 50
    return 0


def chance(dice):
    """Score calculation using any combination.

    Args:
        dice(list):list of 5 dice values.

    Returns:
        score(int):number of points, or 0 if N/A
    """
    return add_values(dice)
