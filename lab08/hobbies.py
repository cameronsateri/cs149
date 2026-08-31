"""

Lab 08.1- prints out list of hobbys and count of each.

Author: Cameron Sateri
Date: 9/22/22
Honor Code:
"""
# input their hobbies, my hobbies, and a combo of the two.
hobbies = ["Baseball", "Lacrosse", "Watching movies",
           "Welding", "Playing instrument"]
my_hobbies = ["Watching movies", "Playing tennis", "Skiing",
              "Spending time with people", "Trying new things"]
our_hobbies = hobbies + my_hobbies
common_hobbies = []
# print out all hobbies
print(our_hobbies)
# determine number of each hobby and condense dupes.
temp = 0
for x in our_hobbies:
    print(x, "=", our_hobbies.count(x))
    if our_hobbies.count(x) > 1:
        common_hobbies.append(x)
        our_hobbies.reverse()
        our_hobbies.remove(x)
        our_hobbies.reverse()
    temp = temp + 1
# prints final outcome. saves fav hobby.
print(our_hobbies)
fav_hobby = our_hobbies[7]
# closing statement.
print("My favorite one is", fav_hobby)
print("\nMy favorite hobby starts with ", fav_hobby[0],
      " and ends with ", fav_hobby[-1], ".", sep="")
print("\nCan you guess what it is?")
