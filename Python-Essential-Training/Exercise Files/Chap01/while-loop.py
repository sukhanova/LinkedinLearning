#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

name = input("What's your name? ")

# TODO: Ask the user by name if they understand Python while loops

question_to_user = input("{}, do you understand Python while loop? (yes/no): ".format(name))

# TODO: Write a while statement that checks if the user doesn't understand while loops
while question_to_user != "yes":
  
# TODO: Since the user doesn't understand while loops, let's explain them.
  print("Ok, {}, while loop we can execute a set of statements as long as a condition is true".format(name))  
# TODO: Ask the user again, by name, if they understand while loops.
  question_to_user = input("{}, do you understand Python while loop? (yes/no): ".format(name))
  
# TODO: Outside the while loop, congratulate the user for understanding while loops
print("You are doing great, {}. Glad you understand Python while loop.".format(name)) 
