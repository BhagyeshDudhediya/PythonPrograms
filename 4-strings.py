#!/usr/bin/python3

# This demonstrates the use of numbers in perl.
# It also shows the way a variable is created and interpreted in python

import sys;

##### STRINGS #####
# Python allows either pair of single or double quotes.
# Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes
# starting at 0 in the beginning of the string and working their way from -1 to the end. 
# The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator

print("\n### STRING IN PYTHON ###")
str = 'Hello World!'
print ("str=", str)          # Prints complete string
print ("str[0]=", str[0])       # Prints first character of the string
print ("str[2:5]=", str[2:5])     # Prints characters starting from 3rd to 5th
print ("str[2:]", str[2:])      # Prints string starting from 3rd character
print ("str * 2=", str * 2)      # Prints string two times
print ("str + TEST=", str + "TEST") # Prints concatenated string



