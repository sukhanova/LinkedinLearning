# function a block of reusable code that is used to perform a single action


def greeting():
    name = input("Please enter your name:")
    time = input("Please enter the time of the day (morning/afternoon/evening):")
    print(name)
    print(time)
    print("Good " + time + ",  " + name + "!")
    

greeting()


def greet(name, time):
    print("Good " + time + ", " + name +"!")
    
greet("Oliver", "day")


def addFive(x):
    print(x+5)
    
addFive(12)
addFive(3.14156)


def square(x):
    return (x * x)

square(121)
result = square(17)
print(result)

anotherOne = square(result)
print(anotherOne)


def sumOfSquares(x, y):
    square1 = x * x
    square2 = y * y
    return square1 + square2

result = sumOfSquares(2, 3)
print(result)


def is_it_raining():
    raining = input("Is it raining today?")
    return raining

# monday_rain = is_it_raining()
# print(monday_rain)

tuesday_rain = is_it_raining()
print(tuesday_rain)