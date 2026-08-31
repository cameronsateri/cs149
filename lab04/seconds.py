"""
Lab 04 - converting large number of seconds into hours, minutes and seconds.

:Author Cameron Sateri
:Version 9/7/22
Honor Code:
"""
ts = int(input("Enter the number of seconds: "))
m = int(ts / 60)
rs = int(ts % 60)
h = int(m / 60)
rm = int(m % 60)
print()
print(ts, "seconds =", h, "hours,", rm, "minutes, and", rs, "seconds\n")
