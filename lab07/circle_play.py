"""

Lab 07- calculates the area and volume of a circle and sphere.

Author: Cameron Sateri
Date: 9/16/22
Honor Code:
"""
import math


# create functions and their definitions.
def print_greeting():
    """
     Prints a greeting when the program is ran by the user.
    """
    print("Welcome to the CS149 Circle Calculator\n")
    print("This application will calculate the area ", end="")
    print("of a circle and/or volume of a sphere.\n")


def enter_radius():
    """
     Displays a prompt to the user, then reads in a float value
     that the user has entered.
     :return a float value representing a radius
    """
    inputradius = float(input("Enter the radius: "))
    return inputradius


def calculate_area(radius):
    """
     Calculates the area of a circle with a given radius.
     :param the given value of the radius
    """
    area = math.pi * math.pow(radius, 2)
    return area


def calculate_volume(radius):
    """
     Calculates the volume of a sphere with a given radius.
     :param the given value of the radius
    """
    volume = (4 / 3) * math.pi * math.pow(radius, 3)
    return volume


# main running lines of code.
print_greeting()
rad = enter_radius()
print("The area of the circle is", calculate_area(rad))
print("The volume of the circle (as a sphere) is", calculate_volume(rad))
