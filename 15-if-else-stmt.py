#!/usr/bin/python3

# use of if, else, elif

num=int(input("enter number: "))

# If the suite of an if clause consists only of a single line,
# it may go on the same line as the header statement
if (num == 1008): print ("num is 1008")

if num%2==0:
    if num%3==0:
        print (num, "Divisible by 3 and 2")
    else:
        print (num, "Divisible by 2 not divisible by 3")
else:
    if num%3==0:
        print (num, "Divisible by 3 not divisible by 2")
    else:
        print  (num, "Not Divisible by 2 not divisible by 3")

num1=int(input("Enter number1: "))
num2=int(input("Enter number2: "))
if num1>num2:
    print ("number1 > number2")
elif num1<num2:
    print ("number1 < number2")
else:
    print ("number1 == number2")
