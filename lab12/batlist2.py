"""Lab 12.

This file holds the four solutions from codingbat in one file.

Author: Cameron Sateri
Version: 10/18/22

Honor Code and Acknowledgments:
    This work complies with the JMU Honor Code.
"""


def count_evens(nums):
    """Counts the number of even values in a list.

    If the number is even, it counts it to return at the end.

    Args:
        nums (list): the full list of numbers to examine.

    Returns:
        ret = total number of evens in list.

    """
    ret = 0
    for x in nums:
        if x % 2 == 0:
            ret = ret + 1
    return ret


def big_diff(nums):
    """Calculates the range of the list.

    Finds the largest and smallest numbers in a list, then
    returns the difference of those values.

    Args:
        nums (list): the full list of numbers to examine.

    Returns:
        Difference between max and min.

    """
    mini = nums[0]
    maxi = nums[0]
    for x in nums:
        mini = min(mini, x)
        maxi = max(maxi, x)
    return maxi - mini


def centered_average(nums):
    """Finds the average besides the largest and smallest.

    Finds the largest and smallest numbers and returns the average
    of the list without those numbers.

    Args:
        nums (list): the full list of numbers to examine.

    Returns:
        The sum minus the max and min divided by the length minus two.

    """
    mini = nums[0]
    maxi = nums[0]
    for x in nums:
        mini = min(mini, x)
        maxi = max(maxi, x)
    return (sum(nums) - mini - maxi) / (len(nums) - 2)


def sum13(nums):
    """Calculates the sum of the list minus any 13s and the following values.

    Finds the number 13 in a list and removes them and the number following
    them in the list from the list.

    Args:
        nums (list): the full list of numbers to examine.

    Returns:
        The sum of nums after being altered.

    """
    r = 0
    while nums.count(13) > 0:
        r = nums.index(13)
        nums.remove(13)
        if r >= len(nums):
            break
        nums.pop(r)
    return sum(nums)
