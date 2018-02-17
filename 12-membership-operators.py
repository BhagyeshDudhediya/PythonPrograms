# Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples.
# There are two membership operators as explained below- 
# in     => Evaluates to true, if it finds a variable in the specified sequence and false otherwise. 
# not in => Evaluates to true, if it does not find a variable in the specified sequence and false otherwise. 

#!/usr/bin/python3 
 
a = 10 
b = 20 
list = [1, 2, 3, 4, 5 ] 
 
print ("a:",a,"b:",b)
print ("List:", list)
if ( a in list ): 
# x not in y, here not in results in a 1 if x is not a member of sequence y.
   print ("Line 1 - a is available in the given list") 
else: 
   print ("Line 1 - a is not available in the given list") 
 
if ( b not in list ): 
   print ("Line 2 - b is not available in the given list") 
else: 
   print ("Line 2 - b is available in the given list") 
 
c=b/a
print ("Value of c=a/b: ",c)
if ( c in list ): 
   print ("Line 3 - c is available in the given list") 
else: 
    print ("Line 3 - c is not available in the given list") 
