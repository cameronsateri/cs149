"""

Lab 9 - calculates monthly charges on a card.

Author: Cameron Sateri
Date: 10/4/22
Honor Code:
"""
prev_bal = float(input("Previous balance: "))
add_charges = float(input("Additional charges: "))
interest = 0.0
if prev_bal > 0:
    interest = (prev_bal + add_charges) * 0.02
new_bal = prev_bal + add_charges + interest
min_pay = 0
if new_bal >= 0 and new_bal <= 49.99:
    min_pay = new_bal
elif new_bal >= 50 and new_bal <= 300:
    min_pay = 50
elif new_bal > 300:
    min_pay = new_bal * 0.2