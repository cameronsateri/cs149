"""Homework 6.2.

This code creates and stores values for colors.

Author: Cameron Sateri
Version: 10/11/22

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


def adjust_brightness(tupcolor, aos):
    """Adjusts colors in a sequence based on value.

    Args:
        tupcolor (tupple): length-three tuple representing a color.
        aos (int): value (positive or negative) that will be added to each color channel.

    Returns:
        ret (tupple): length-three tuple representing the altered color.
    """
    q = [0, 0, 0]
    for x in range(3):
        q[x] = tupcolor[x] + aos
        if q[x] < 0:
            q[x] = 0
        elif q[x] > 255:
            q[x] = 255
    ret = (q[0], q[1], q[2])
    return ret


def same_color(colora, colorb, dif):
    """Determines the similarity between two colors.

    Args:
        colora (tupple): first color to be compared.
        colorb (tupple): second color to be comapred.
        dif (int): value representing the max difference in numbers

    Returns:
        true: all 3 values are at most the value of dif.
        false: one or more values are more than dif.
    """
    x = 0
    while x < 3:
        t = abs(colora[x] - colorb[x])
        if t > dif:
            return False
        x = x + 1
    return True
