#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

attendees = ["Oliver", "Jen", "Brian", "Holly", "Mary", "Jeff"]
print("There are", len(attendees), "attendees currently.")
attendees.append("Cora")
attendees.extend(["John", "Mariah"])
optional_invitees = ["Gary", "Amy"]
potential_attendees = attendees + optional_invitees
print("New number of attendees is:", len(potential_attendees))


# add items to the list
fruits_in_busket = []
fruits_in_busket.append("apples")
fruits_in_busket.append("plums")
fruits_in_busket.append("apples")
print(fruits_in_busket)
fruits_on_plate = ["kiwi", "pears", "oranges"]

# combine lists:
# fruits_in_busket.extend(fruits_on_plate)
# print(fruits_in_busket)

all_fruits = fruits_in_busket + fruits_on_plate
print(all_fruits)

