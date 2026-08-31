"""

Lab 06- print out rose art.

Author: Cameron Sateri
Date: 9/13/22
Honor Code:
"""
# create inital rose values.
rose1 = (2, 4, 3)
rose2 = (5, 1, 2)
rose3 = (5, 7, 2)
rose4 = (1, 1, 10)
rose5 = (1, 1, 1)
# determine longest rose.
# note that 3 is added to each to include seperations of the stem.
tlengths = []
tlengths.insert(0, rose1[0] + rose1[1] + rose1[2] + 3)
tlengths.insert(1, rose2[0] + rose2[1] + rose2[2] + 3)
tlengths.insert(2, rose3[0] + rose3[1] + rose3[2] + 3)
tlengths.insert(3, rose4[0] + rose4[1] + rose4[2] + 3)
tlengths.insert(4, rose5[0] + rose5[1] + rose5[2] + 3)
hlength = max(tlengths)
# print out the roses.
# each rose is 2 lines.
print((hlength - tlengths[0]) * " ", "@", rose1[0] * "-", ">",
      rose1[1] * "-", ">", rose1[2] * "-", sep="")
print((hlength - tlengths[1]) * " ", "@", rose2[0] * "-", ">",
      rose2[1] * "-", ">", rose2[2] * "-", sep="")
print((hlength - tlengths[2]) * " ", "@", rose3[0] * "-", ">",
      rose3[1] * "-", ">", rose3[2] * "-", sep="")
print((hlength - tlengths[3]) * " ", "@", rose4[0] * "-", ">",
      rose4[1] * "-", ">", rose4[2] * "-", sep="")
print((hlength - tlengths[4]) * " ", "@", rose5[0] * "-", ">",
      rose5[1] * "-", ">", rose5[2] * "-", sep="")
