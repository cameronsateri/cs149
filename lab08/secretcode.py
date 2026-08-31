"""

Lab 08.4- .

Author: Cameron Sateri
Date: 9/25/22
Honor Code:
"""
# generate first name, last name, full name, and birth year.
first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
full_name = first_name + " " + last_name
birth_year = int(input("Enter your birth year: "))
print("\nThe name you have provided is:", full_name)

# generate codename.
numa = len(full_name) - 1 + birth_year
numb = numa // len(last_name)
secret_passcode = first_name[0] + first_name[1] + str(numb) + last_name[-2].upper() + last_name[-1]
print(f"\nYour secret passcode is: {secret_passcode}")