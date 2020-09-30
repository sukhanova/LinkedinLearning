#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import math

print('Hello, World.')


#function to split check between friends

# total = input("What's your total for a meal? ")
# number_of_people = input("How many people were dining in together? ")


def split_check(total_due, number_of_people):
  # cost_per_person = math.ceil(cost_per_person)
  # return cost_per_person
  if number_of_people <= 1:
    raise ValueError("More than 1 person required to split check")
  return round(total_due / number_of_people, 2)

try:
  total_due = float(input("What is your total? "))
  number_of_people = int(input("How many people? "))
  amount_due = split_check(total_due, number_of_people)
except ValueError as error:
  print("That's not valid value. Try again - this time numbers only....")
  print("({})".format(error))
else:
  print("Each person owes ${}".format(amount_due))
