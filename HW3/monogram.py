name_first = input("First name? ")
name_middle = input("Middle name? ")
name_last = input("Last name? ")
name = name_first + " " + name_middle + " " + name_last
initials = name_first[0] + name_middle[0] + name_last[0]
print("\nThe customer ", name, " has ordered a sweater with the monogram ", initials, ".", sep="")
