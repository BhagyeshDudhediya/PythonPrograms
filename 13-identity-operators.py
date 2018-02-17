# Identity operators compare the memory locations of two objects. There are two Identity operators as explained below: 
# Operator Description Example 
# is     => Evaluates to true if the variables on either side of the operator point to the same object and false otherwise. 
#           x is y, here is results in 1 if id(x) equals id(y). 
# is not => Evaluates to false if the variables on either side of the operator point to the same object and true otherwise. 
#           x is not y, here is not results in 1 if id(x) is not equal to id(y). 

#!/usr/bin/python3

a = 20
b = 20
print ('Line 1','a=',a,':',id(a), 'b=',b,':',id(b))

if ( a is b ):
   print ("Line 2 - a and b have same identity")
else:
   print ("Line 2 - a and b do not have same identity")

if ( id(a) == id(b) ):
   print ("Line 3 - a and b have same identity")
else:
   print ("Line 3 - a and b do not have same identity")

b = 30
print ('Line 4','a=',a,':',id(a), 'b=',b,':',id(b))

if ( a is not b ):
   print ("Line 5 - a and b do not have same identity")
else:
   print ("Line 5 - a and b have same identity")
