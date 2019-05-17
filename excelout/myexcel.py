#!/usr/bin/env python3

## sudo apt install python3-pip

## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls

import pyexcel
import datetime

#Request data from user

def get_ip_data ():
	input_ip = input ("\nWhat is the IP address? ")
	input_driver = inpu("\nWhat is the driver associated with this device? ")
	d = {"IP" : input_ip, "driver": input_driver}
	return d

# Runtime
mylistdict = []

print ("Hello! This program will make you a *.xls file")

While (True)
    mylistdict.append(mylistdict())
    keep_going = input ("\nWould you like to add another value? Enter to continue, or enter 'q' to quit")
        if keep.going.lower() =='q':
        break

today = dt.datetime.now().strftime("%Y-%m-%d")
filename = input ("\nWhat is the name of the *.xls file? ")
filename = today + "." + filename + ".xls"

pyexcel.save as (records=mylistdict, dest_file_name=filename)

print (f"The file {filename} is saved on your local directory")
