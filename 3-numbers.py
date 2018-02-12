#!/usr/bin/python3

# This demonstrates the use of numbers in perl.
# It also shows the way a variable is created and interpreted in python

import sys;

# Python variables do not need explicit declaration to reserve memory space. 
# The declaration happens automatically when you assign a value to a variable.


counter = 10    # integer value
miles = 100.0   # floating point number
name = "John"   # string

print ("\nInteger: ", counter, "\nFloating: ", miles, "\nString: ", name);

# Python also allows us to assign single value to multiple variables:
var_1 = var_2 = var_3 = 10;
print("\nSingle value assigned to multiple variables:", var_1, var_2, var_3);

var1, var2, var3 = 1, 2, "John";
print("\nMultiple values assigned to multiple variables:", var1, var2, var3)

# Python has 5 standard data types: numbers, string, list, tuple, dictionary

##### NUMBERS #####
print("\n### NUMBERS IN PYTHON ###")
num1 = 10
num2 = 20
print ("num1=", num1, "num2=", num2);
# You can also delete the reference to a number object by using the del statement
del num1;
num3 = 30
del num2, num3
# The following lines if uncommented gives error: NameError: name 'num1' is not defined 
# del num1, num2
# print ("Numbers: num1=", num1, "num2=", num2)

# A complex number consists of an ordered pair of real floating-point numbers denoted by x + yj,
# where x and y are real numbers and j is the imaginary unit

