#!/usr/bin/env python3
firstlist =[]
mylist = ["cat", "dog" , 7]
print (mylist)

#ouput dog
print (mylist[1])

#I have a cat and a dog that are 7
print (f"I have a {mylist[0]} and a {mylist[1]} that are {mylist[2]}.")

feline = mylist[0]
print (feline)

myvar = ["hamster", "snake"]
#mylist.append("hamster")
mylist.append(myvar)
print (mylist.pop(1))
mylist.insert(1, "squirrel")
print (mylist)

print (mylist[3][1])

print ("my {} string".format ("first"))

