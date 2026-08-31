"""
Lab 03 - Style lab - testing style and gradescope submission
:Author YOUR NAME
:Version 1-26-22
Honor Code:
"""
print("What is your name?", end=' ')
Name = input()
print("How many hours did you work this week?", end=' ')
h = int(input())
print("What is your hourly pay rate?", end=' ')
payrate = float(input())
grosspay = int(h)*float(payrate)
bonus = 500
grosspay = grosspay+bonus
print("Hello " + Name)
print("Your gross pay is $", grosspay)
