#!/usr/bin/env python3

first_dictionary = {}
second = {"car": "malibu", "dream_car": "corvette"}
print (second["car"])
print (second["dream_car"])

second.update({"dream_car": "bugatti"})
print (second)
print (second["dream_car"])

second["car"]="prius"
print(second)
print(second["car"])

#print (second.keys())
#print (second.values())

second["car"]=["prius", "F350", "SantaFe"]
print (second["car"][1])
