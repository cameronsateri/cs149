"""Homework 8.3.

This code applies the shift sypher to a phrase.

Author: Cameron Sateri
Version: 10/28/22

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


def encode(txt, ival):
    """Returns coded version of phrase txt.

    Args:
        txt (str): word to be shifted.
        ival (int): how far the letters should be shifted.

    Returns:
        ret (str): coded version of phrase.
    """
    txt = txt.lower()
    ret = ""
    for x in range(len(txt)):
        value = ord(txt[x])
        if ord(txt[x]) <= 122 and ord(txt[x]) >= 97:
            value = ord(txt[x]) + ival
            if value < 97:
                value = 123 - (97 - value)
            elif value > 122:
                value = 96 + (value - 122)
        ret = f'{ret}{chr(value)}'
    return ret


print(encode("this shouldn't change", 0))
