#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import sys

print('Hello, World.')

MASTER_PASSWORD = 'password'
password = input("Please enter the super secret password: ")
attempt_count = 1
while password != MASTER_PASSWORD:
  if attempt_count > 3:
   sys.exit("Too many invalid password attempts") 
  password = input("Invalid password, please try again: ")
  attempt_count += 1
print("Welcome to secret page!")