#!/usr/bin/python3

import sys;

# Lists are the most versatile of Python's compound data types.
# A list contains items separated by commas and enclosed within square brackets ([]).
# To some extent, lists are similar to arrays in C.
# One of the differences between them is that all the items belonging to a list can be of different data type. 

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print ("list: ", list)                          # Prints complete list
print ("list[0]: ", list[0])                    # Prints first element of the list
print ("list[1:3]: ", list[1:3])                # Prints elements starting from 2nd till 3rd
print ("list[2:]: ", list[2:])                  # Prints elements starting from 3rd element
print ("tinylist *2: ", tinylist * 2)           # Prints list two times
print ("list + tinylist: ", list + tinylist)    # Prints concatenated lists

# Lists in python are read-write list, we can change the value of a list variable
list[3] = 'xyz'
print (list)

### TUPLES IN PYTHON ###
print ("\n\n## TUPLES ##")
# A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas.
# Unlike lists, however, tuples are enclosed within parenthesis. 
# The main difference between lists and tuples is- Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed,
# while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')
print ("tuple: ", tuple)                          # Prints complete tuple
print ("tuple[0]: ", tuple[0])                    # Prints first element of the tuple
print ("tuple[1:3]: ", tuple[1:3])                # Prints elements starting from 2nd till 3rd
print ("tuple[2:]: ", tuple[2:])                  # Prints elements starting from 3rd element
print ("tinytuple *2: ", tinytuple * 2)           # Prints tuple two times
print ("tuple + tinytuple: ", tuple + tinytuple)    # Prints concatenated tuples

# Tuples are just readbale, one cannot modify any element in tuple
# Following line when uncommented throws error: TypeError: 'tuple' object does not support item assignment
# tuple[2] = 123
