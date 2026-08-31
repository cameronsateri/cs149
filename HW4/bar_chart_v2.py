"""Print a nicely formatted bar chart.

Author: Cameron Sateri
Version: 10/6/22
"""
import math


def print_bar(label, length):
    """Print a single row of a bar chart.

    The length argument will be converted to an int in order to determine the
    number of "=" symbols to use.

    for example:

    >>> print_bar("Ruby", 3.9)
    Ruby     : ===

    Args:
        label (str): The label for this bar
        length (float): The length of the bar
    """
    if len(label) >= 8:
        label = label[0:8]
    print(label, " " * (9 - len(label)), ": ", "=" * math.floor(length), sep="")


def print_border(data):
    """Print a correctly-sized border of '-' characters.

    Print a number of '-' symbols equal to the maximum value in data
    (converted to an integer), plus 11.

    Args:
        data: A list of floats
    """
    biggest_data = 0
    x = 0
    if data[x] > biggest_data:
        biggest_data = data[x]
    x = x + 1
    if data[x] > biggest_data:
        biggest_data = data[x]
    x = x + 1
    if data[x] > biggest_data:
        biggest_data = data[x]
    x = x + 1
    if data[x] > biggest_data:
        biggest_data = data[x]
    x = x + 1
    if data[x] > biggest_data:
        biggest_data = data[x]
    bar_length = math.floor(biggest_data) + 11
    print("-" * bar_length)
    

def min_max(data):
    x = 0
    biggest_data = data[0]
    lowest_data = data[0]
    if data[x] > biggest_data:
        biggest_data = data[x]
    if data[x] < lowest_data:
        lowest_data = data[x]
    x = x + 1
    if data[x] > biggest_data:
        biggest_data = data[x]
    if data[x] < lowest_data:
        lowest_data = data[x]
    x = x + 1
    if data[x] > biggest_data:
        biggest_data = data[x]
    if data[x] < lowest_data:
        lowest_data = data[x]
    x = x + 1
    if data[x] > biggest_data:
        biggest_data = data[x]
    if data[x] < lowest_data:
        lowest_data = data[x]
    x = x + 1
    if data[x] > biggest_data:
        biggest_data = data[x]
    if data[x] < lowest_data:
        lowest_data = data[x]
    print("min:", "{:,.2f}".format(lowest_data), "max:", "{:,.2f}".format(biggest_data))


def print_bar_chart(labels, data):
    """Print a nicely formatted bar chart.

    The chart will have one row for each of the five entries in the two
    provided lists.

    Args:
        labels: A list of label strings
        data: A list of floats that will determine the length of the bars
    """
    print_border(data)
    x = 0
    print_bar(labels[x], data[x])
    x = x + 1
    print_bar(labels[x], data[x])
    x = x + 1
    print_bar(labels[x], data[x])
    x = x + 1
    print_bar(labels[x], data[x])
    x = x + 1
    print_bar(labels[x], data[x])
    print_border(data)
    min_max(data)
    

if __name__ == "__main__":

    # Don't change this!  Just finish the functions above.

    l1 = ['Python', 'Java', 'JavaScript', 'C#', 'PHP']
    d1 = [29.9, 19.1, 8.2, 7.3, 6.2]
    print_bar_chart(l1, d1)
