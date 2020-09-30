#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')
#print('Python Essential Training')


print(bool(1))
print(bool())

fruit = "pear"

print(fruit == "Pear")

first_name = input("What is your name? ")
# print("Hello,", first_name)
if(first_name == "Oliver"):
    print("Hello and welcome back,", first_name)
else:
    print("Hello, {}".format(first_name))