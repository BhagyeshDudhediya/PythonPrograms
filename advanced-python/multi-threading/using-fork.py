import os

# This will fail on windows as fork() is not defined for windows machine
# fork() returns 2 values, it returns 0 in child's context and returns
# non-negative value (childs PID) in parents context
# When a process is forked, everything including a program counter is shared
# between child and parent. Hence, both child and parent will start executing
# the same code after fork as program counter points to the statement
# after call to fork()

var = 100               # global variable
x=os.fork()
# hi will be printed twice, one is child's conext and one in parent's context
print ('hi')

if (x==-1):
    print "Error while forking"
elif (x == 0):
    print "I am a child process"
    print "CHILD: "+str(x),str(os.getpid())
    # Change the value of global variable in child and check if it's same in parent as well
    global var
    var = 20
    print "Value of var after changing in child="+str(var)
else:
    print "I am a parent process"
    print "PARENT: "+str(x),str(os.getpid())
    print "Value of var in parent="+str(var)
