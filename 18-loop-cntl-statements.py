#!/usr/bin/python3

# The Loop control statements change the execution from its normal sequence. When the execution leaves a scope,
# all automatic objects that were created in that scope are destroyed. 
# There are 3 loop control statements:
# 1. break, 2. continue, 3. pass

# BREAK STATEMENT
# The break statement is used for premature termination of the current loop. After abandoning the loop,
# execution at the next statement is resumed, just like the traditional break statement in C.
# The most common use of break is when some external condition is triggered requiring a hasty exit from a loop.
# The break statement can be used in both while and for loops.
# If you are using nested loops, the break statement stops the execution of the innermost loop and
# starts executing the next line of the code after the block. 
print ('Break Statement:');
my_num=int(input('any number: '))
numbers=[11,33,55,39,55,75,37,21,23,41,13]
print ('list', numbers);
for num in numbers:
    if num==my_num:
        print ('number',my_num,'found in list')
        break
else:
    print ('number',my_num,'not found in list')

# CONTINUE STATEMENT
# The continue statement in Python returns the control to the beginning of the current loop.
# When encountered, the loop starts next iteration without executing the remaining statements in the current iteration.
# The continue statement can be used in both while and for loops.
print ('\nContinue Statement:');
var = 10                    # Second Example
while var > 0:
    var = var - 1;
    if var == 5:
        print ("var == 5, so continue..")
        continue
    print ('Current variable value :', var)

# PASS STATEMENT
# It is used when a statement is required syntactically but you do not want any command or code to execute.
# The pass statement is a null operation; nothing happens when it executes. The pass statement is also
# useful in places where your code will eventually go, but has not been written yet i.e. in stubs).
print ('\nPass Statement')
for letter in 'Python':
    if letter == 'h':
        pass
        print ('This is pass block')
    print ('Current Letter :', letter)
    
