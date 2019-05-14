#!/usr/bin/env python3
firstlist =[]
first_dict = {"first_name": "Monty", "last_name": "Python", "actions": ["Scooter", 2, "Moscow"]}

# name["key"][index]

print (f'In {first_dict["first_name"]} {first_dict["last_name"]}, Eric Idle rode a {first_dict["actions"][0]} {first_dict["actions"][1]} {first_dict["actions"][2]}. ')

print()

print (f"In {first_dict['first_name']} {first_dict['last_name']}, Eric Idle rode a {first_dict['actions'][0]} {first_dict['actions'][1]} {first_dict['actions'][2]}. ")


firstlist.append("horse")
print(firstlist)
firstlist.extend(["to","the Holy Grail"])
print(firstlist)
#####

second_list = ["horse", "to", "the Holy Grail"]
first_dict.update ({"actions": firslist})
print (firstlist)
