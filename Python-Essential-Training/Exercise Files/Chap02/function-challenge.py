#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#TASK #1
# Create a function that determines if a specific value is odd.
# Name the function is_odd and have it declare a single parameter.
# It should return True if the value is not divisible by 2.

def is_odd(par):
  if par % 2 == 0:
    return False
  else:
    return True

print(is_odd(4))
print(is_odd(5))
print(is_odd(6))
print(is_odd(7))


#TASK #2
"""
This is importing a function named `tweet` from a file
    that we unfortunately don't have access to change.

You use it like so:
>>> tweet("Hello this is my tweet")

If the function cannot connect to Twitter,
    the function will raise a `CommunicationError`
If the message is too long,
    the function will raise a `MessageTooLongError`
"""
from twitter import (
    tweet,
    MessageTooLongError,
    CommunicationError,
)

message = input("What would you like to tweet?  ")
# Your code here
try:
    tweet(message)
    # tweet ---> your function name
    # message ---> your variable
except CommunicationError:
    print("An error occurred attempting to connect to Twitter.  Please try again!")
except MessageTooLongError as e:
    print("Oh no! Your message was too long ({})".format(e))

# tweet ---> your function name
# message ---> your variable