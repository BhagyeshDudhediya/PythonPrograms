#!/usr/bin/python3

# A while loop statement in Python programming language repeatedly executes a target statement as long as a given condition is true. 
# Syntax:
# The syntax of a while loop in Python programming language is- 
# while expression: 
#    statement(s) 
# Here, statement(s) may be a single statement or a block of statements with uniform indent.
# The condition may be any expression, and true is any non-zero value. The loop iterates while the condition is true. 
# When the condition becomes false, program control passes to the line immediately following the loop.
# When the condition is tested and the result is false, the loop body will be skipped and the first
# statement after the while loop will be executed.

count = 0 
while count < 5: 
   print (count, " is  less than 5") 
   count = count + 1 

# Python supports having an else statement associated with a loop statement
# If the else statement is used with a while loop, the else statement is executed when the condition becomes false.
else: 
   print (count, " is not less than 5") 
