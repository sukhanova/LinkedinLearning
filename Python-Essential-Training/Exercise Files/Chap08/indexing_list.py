#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# Indexing in Python is zero-based

# Add to the list:

books = [
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]
print(books[0])
books[1] = "Python for Data Analisys - Wes McKinney"
print(books[len(books)-1])

print("Suggested gift: {}.".format(books[0]))

print(books[0])
# insert book to specific point of the list
books.insert(0, "Learning Python: Powerful Object-Oriented Programming")
books[0] += " - Mark Lutz"
print(books[0])


# Delete from the list:

books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

print("Suggested gift: {}".format(books[0]))

# remove specific item from list
recommendation = books[0]
del books[0]
print(books)
print(recommendation)

# remove last item from list
test = books.pop()
print(test)

books.pop(0)
print(books)
