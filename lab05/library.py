"""

Lab 5 - trade books within the items in the library.

Author: Cameron Sateri
Date: 9/8/22
Honor Code:
"""
books = ["Project Hail Mary", "The Hobbit", "Sherlock Holmes", "The Hobbit", "Dune"]
print("= Little Free Library =")
print("Count:", len(books), "book(s)")
print(books)
print()
inter = input("Enter the title of a book to find: ")
te = books.index(inter)
print("We have ", books.count(inter), " copies of \"", str(books[te]), "\" available.", sep="")
take = int(input("Enter the index of a book to take: "))
print("You took \"", books[take], "\".", sep="")
del books[take]
print(books)
print()
leave = input("What book would you like to leave? ")
books.append(leave)
print(books)

