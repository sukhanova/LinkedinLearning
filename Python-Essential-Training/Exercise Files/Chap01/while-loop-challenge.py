#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

TICKET_PRICE = 10

ticket_remaining = 100

# Output how many tickets are remaining using the tickets_remaining variable

print("There are {} tickets remaining".format(ticket_remaining))

# Gather the user's name and assign to the new variable

name = input("Hello there! What's your name? ")

# Prompt user by name and ask how many tickets they would like
num_tickets = input("How many tickets would you like to buy today, {}? ".format(name))
num_tickets = int(num_tickets)

# Calculate the total (number of tickets multiply by the price) and assign to the variable
amount_due = num_tickets * TICKET_PRICE

# Output the price to the screen
print("{}, your total today is ${}".format(name, amount_due))