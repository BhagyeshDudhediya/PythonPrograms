#!/usr/bin/python3

# The for statement in Python has the ability to iterate over the items of any sequence, such as a list or a string.
# Syntax
# for iterating_var in sequence:
#    statements(s)
# If a sequence contains an expression list, it is evaluated first. Then, the first item in the sequence is assigned
# to the iterating variable iterating_var.
# Next, the statements block is executed. Each item in the list is assigned to iterating_var,
# and the statement(s) block is executed until the entire sequence is exhausted

# Traversing a string
print ("For loop with string traversal:");
for letter in 'Python':     # traversal of a string sequence
   print ('Current Letter :', letter);

# Traversing a list
print ("\nFor loop with list traversal");
fruits = ['banana', 'apple', 'mango'];
for fruit in fruits:
    print ("Current Fruit:", fruit);

# The built-in function range() is the right function to iterate over a sequence of numbers. It generates
# an iterator to progress integers starting with 0 upto n-1. To obtain a list object of the sequence,
# it is typecasted to list(). Now this list can be iterated using the for statement

print("\nFor loop with range() function:");
even_nums=odd_nums="";
for var in list(range(10)):
        if (var%2 == 0):
            even_nums += str(var)+",";
        else:
            odd_nums += str(var)+",";
print ("Even Numbers:", even_nums);
print ("Odd Numbers:", odd_nums);

# Iterating by index sequence
# An alternative way of iterating through each item is by index offset into the sequence itself.
print ("\nIterating a list using index")
sports = ['cricket', 'kho-kho', 'kabaddi', 'foosball'];
for index in range(len(sports)):
    print ("sports[",index,"] = ", sports[index])

# For loop with else statement
# If the else statement is used with a for loop, the else block is executed only if for loops
# terminates normally (and not by encountering break statement).
numbers=[11,33,55,39,55,75,37,21,23,41,13]
print("\nlist:", numbers);
print ("For loop with else statement without break:");
for num in numbers: 
    if num%2==0: 
        print ('The list contains an even number');
        break;
else: 
    # This will be executed as loop ends because normally without break stmt
    print ('The list doesnot contain even number');

print ("\nFor loop with else statement with break:");
for num in numbers: 
    if num%2!=0: 
        print ('The list contains an odd number');
        break;
else:
    # This will not be executed as loop ends because of break stmt
    print ('The list doesnot contain odd number');

# Python programming language allows the use of one loop inside another loop. The following section shows a few examples to illustrate the concept. 
# Syntax 
# for iterating_var in sequence: 
#    for iterating_var in sequence: 
#       statements(s) 
#    statements(s) 
#
# The syntax for a nested while loop statement in Python programming language is as follows- 
# while expression: 
#    while expression: 
#       statement(s) 
#    statement(s) 
# A final note on loop nesting is that you can put any type of loop inside any other type of loop.
# For example a for loop can be inside a while loop or vice versa. 
print ("\nNested Loops in Python:") 
for i in range(1,11): 
    for j in range(1,11): 
        k = i*j
        #  end=' ' appends a space instead of default newline. Hence, the numbers will appear in one row.
        print (k, end=' ');
    print ();
