"""

Lab 08.2- stores dictionary values and list
values of classmates and their homes.

Author: Cameron Sateri
Date: 9/22/22
Honor Code:
"""
# create dictionary with names and hometowns, also makes hometown empty list.
classmate_home = {"Cameron": "Ashburn", "Kody": "Leesburg",
                  "Kyla": "Lewisburg", "Joshua": "Alexandria",
                  "Samantha": "Leesburg"}
hometowns = []

# fill hometowns with classmate homes.
hometowns.append(classmate_home["Cameron"])
hometowns.append(classmate_home["Kody"])
hometowns.append(classmate_home["Kyla"])
hometowns.append(classmate_home["Joshua"])
hometowns.append(classmate_home["Samantha"])

# update dictionary with new item.
classmate_home["Shrestha"] = "Nepal"
hometowns.append(classmate_home["Shrestha"])

# alter new dictionary item and value.
hometowns[-1] = "Virginia"
classmate_home["Shrestha"] = hometowns[-1]

# print list and dictionary.
print(hometowns)
print(classmate_home)
