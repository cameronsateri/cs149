"""

Lab 08.3- creates greetings and randomly greets labmate.

Author: Cameron Sateri
Date: 9/22/22
Honor Code:
"""
import random

# empty dictionary.
greetings = {}

# adds 6 items and respective keys.
greetings[1] = "Hi! You’re going to have a great day today."
greetings[2] = "Greetings, I see your day being productive. Good Luck."
greetings[3] = "I hope you have a wonderful day!"
greetings[4] = "Today maybe the day you find answers. Best!"
greetings[5] = "I believe you can make this world better."
greetings[6] = "We will have a great day."

# prints greetings.
print(greetings)

# store labmates name. random number generation.
labmate = "Kody"
random_num = random.randint(1, 6)

# print labmates name and random greeting
print(labmate, ", ", greetings[random_num], sep="")
