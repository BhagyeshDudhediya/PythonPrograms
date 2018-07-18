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

## FUNCTIONS WITH NUMBERS:

# The abs() method returns the absolute value of x i.e. the positive distance between x and zero
print ('\n=== abs() function ===')
print ('abs(-45)=', abs(-45));
print ('abs(100.12)=', abs(100.12));

# The ceil() method returns the ceiling value of x i.e. the smallest integer not less than x i.e first integer
# which is greater than x
# It required math module to be imported
print ('\n=== math.ceil() function ===')
import math;
print ('math.ceil(4.5)=', math.ceil(4.5))
print ('math.ceil(-45.17)=', math.ceil(-45.17))     # prints -45 as -45 > -45.17
print ('math.ceil(math.pi)=', math.ceil(math.pi))

# The floor() method returns the floor of x i.e. the largest integer not greater than x i.e integer
# just behind it
print ('\n=== math.floor() function ===')
print ('math.floor(4.5)=', math.floor(4.5))
print ('math.floor(-45.17)=', math.floor(-45.17))     # prints -46 as -46 < -45.17
print ('math.floor(math.pi)=', math.floor(math.pi))

print ('\n=== math.exp() function ===')
print ('math.exp(-45.17)=', math.exp(-45.17))   #  2.4150062132629406e-20 i.e e-20 is 10 to the power -20
print ("math.exp(math.pi)=", math.exp(math.pi))

# The log() method returns the natural logarithm of x, for x > 0. 
print ('\n=== math.log() function ===')
print ('math.log(4.5)=', math.log(4.5))
print ('math.log(math.pi)=', math.log(math.pi))

# The log10() method returns base-10 logarithm of x for x > 0. 
print ('\n=== math.log10() function ===')
print ('math.log10(104.5)=', math.log10(104.5))
print ('math.log10(math.pi)=', math.log10(math.pi))

# The max() method returns the largest of its arguments i.e. the value closest to positive infinity.
# Syntax:
# max( x, y, z, .... )
# Parameters x,y,z - are numeric expression.
print ('\n=== max() function ===')
print ("max(80, 100, 1000) : ", max(80, 100, 1000))
print ("max(-20, 100, 400) : ", max(-20, 100, 400))
print ("max(-80, -20, -10) : ", max(-80, -20, -10))

# The min() method returns the largest of its arguments i.e. the value closest to positive infinity.
# Syntax:
# min( x, y, z, .... )
# Parameters x,y,z - are numeric expression.
print ('\n=== min() function ===')
print ("min(80, 100, 1000) : ", min(80, 100, 1000))
print ("min(-20, 100, 400) : ", min(-20, 100, 400))
print ("min(-80, -20, -10) : ", min(-80, -20, -10))

# The modf() method returns the fractional and integer parts of x in a two-item tuple. Both parts have the same sign as x.
# The integer part is returned as a float. It divides number into 2 parts.
print ('\n=== math.modf() function ===')
print ("math.modf(100.12)=", math.modf(100.12))
print ("math.modf(100.72)=", math.modf(100.72))
print ("math.modf(119)=", math.modf(119))
print ("math.modf(math.pi)=", math.modf(math.pi)) 
