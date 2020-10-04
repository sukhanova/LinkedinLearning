#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

TICKET_PRICE = 10
SERVICE_CHARGE = 2

ticket_remaining = 100

def calculate_price(num_of_tickets):
  return (num_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while ticket_remaining >= 1:
  print("There are {} tickets remaining".format(ticket_remaining))
  name = input("Hello there! What's your name? ")
  num_tickets = input("How many tickets would you like to buy today, {}? ".format(name))
  try:
    num_tickets = int(num_tickets)
    if num_tickets > ticket_remaining:
      raise ValueError("There are only {} tickets remaining".format(ticket_remaining))
  except ValueError as error:
    print("There is an issue with an input. {}. Please try again later!".format(error))
  else:
    amount_due = calculate_price(num_tickets)
    print("{}, your total today is ${}".format(name, amount_due))
    should_proceed = input("{}, There are {} tickets in your cart. Would you like to proceed (Y/N)? ".format(name, num_tickets))
    if should_proceed.lower() == "y" or should_proceed.lower() == "yes":
        #TODO: Gather credit card information and process it
        print("SOLD {} tickets to {}!".format(num_tickets, name))
        ticket_remaining -= num_tickets
    else:
      print("Thank you for your interest, {}. Come back again!".format(name))
print("Sorry the tickets are all sold out!! Come back later!")