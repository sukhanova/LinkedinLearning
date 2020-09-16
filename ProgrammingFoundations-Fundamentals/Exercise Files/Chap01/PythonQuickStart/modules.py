# Module is a software component that contains one or more routines

import calendar

cal = calendar.month(2013, 11)
print(cal)


import math

result = math.sqrt(49)
print(result)


x = pow(4, 3)
print(x)


import random

randomNumber = random.randint(1, 10)
print(randomNumber)

movies = ["Aladdin", "Pets 2", "Lion King", "Spider-Man", "Avengers", "Men in Black", "Titanic", "Avatar", "Terminator", "Paddington"]
watch = random.choice(movies)

print(watch)

card = "Jack"
deck = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
print(deck)
random.shuffle(deck)
print(deck)


card = "Jack"
deck = ["Ace", "Two", "Three", "Four", "Five", "Six",
        "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

type(card)
type(deck)