#!/usr/bin/python3

import sys;

# To convert between types, you simply use the type-name as a function
# int(x [,base])            Converts x to an integer. The base specifies the base if x is a string.
# float(x)                  Converts x to a floating-point number.
# complex(real [,imag])     Creates a complex number.
# str(x)                    Converts object x to a string representation.
# repr(x)                   Converts object x to an expression string.
# eval(str)                 Evaluates a string and returns an object.
# tuple(s)                  Converts s to a tuple.
# list(s)                   Converts s to a list.
# set(s)                    Converts s to a set.
# dict(d)                   Creates a dictionary. d must be a sequence of (key,value) tuples.
# frozenset(s)              Converts s to a frozen set.
# chr(x)                    Converts an integer to a character.
# unichr(x)                 Converts an integer to a Unicode character.
# ord(x)                    Converts a single character to its integer value.
# hex(x)                    Converts an integer to a hexadecimal string.
# oct(x)                    Converts an integer to an octal string.

str_val = "15"                  # String with value 10
print ("string to int: ", int(str_val, 10))        # Convert string to integer with base 10

int_val = 25;
print ("number to float: ", float(int_val))      # Convert integer to float
print ("string to float: ", float(str_val))          # Convert string to float

str_val2 = "bhagyesh dudhediya"         # string variable
str_val2_to_tuple = tuple(str_val2)     # Convert string to tuple
print ("string to tuple: ", str_val2_to_tuple)           
#str_val2_to_tuple[1] = "A"             # This fails, as tuple cannot be modified
tuple_to_list = list(str_val2_to_tuple) # Convert tuple to list
print ("tuple to list: ", tuple_to_list)
tuple_to_list[2] = 'A'                  # List members can be modified
print("modified list: ", tuple_to_list)
print ("list to set: ", set(tuple_to_list))  # Convert list to a set, all duplicate members will be removed

list_val = [1, 'bhagyesh', 'john', 'A', 'bhagyesh']
print ("list to frozen set: ", frozenset(list_val)) # Convert list to frozen set

char_val = 'A'
print ("char to integer: ", ord(char_val))      # Convert char to integer
print ("Integer 25 to Octal: ", oct(int_val))   # Convert char to octal
print ("Integer 25 to Hex: ", hex(int_val))     # Convert integer to hex
print ("Integer 99 to char: ", chr(99))         # Convert integer to char

# When we convert set to list, set and list matches, but when we convert list to set, list and set are not same
# because the duplicate elements if any in the list are removed when converted to set.
set_val = {'A', "B", "B", "A"}
print ("Set: ", set_val)
print ("Set to list: ", list(set_val))          # Convert set to list
print ("Set to tuple: ", tuple(set_val))        # Convert set to tuple
