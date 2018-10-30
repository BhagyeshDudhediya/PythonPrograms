import threading
import os

var = 100

def print_square(num):
    print str(os.getpid())+": Sqaure is: "+str(num*num)
    global var
    var = 20
    print (str(str(os.getpid()))+": Value of global var when changed in thread ="+str(var))
    print (str(os.getpid())+": Value of id(x)="+str(id(var)))

def print_cube(num):
    print str(os.getpid())+": Cube is: "+str(num*num*num)

if __name__ == '__main__':
    # Create thread
    print (str(os.getpid())+": Var in main before spawing thread="+str(var))
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(9,))
    
    # Start the thread
    t1.start()
    t2.start()
    
    # Wait for thread to complete before main thread exits
    t1.join()
    t2.join()

    # Thread p1 changes the global variable. Let's check if it is reflected here after p1 is done with it's work
    # Parent thread does a shallow copy and hence there will be change in value of var as child has a shared copy of var
    print (str(os.getpid())+": Var in main after t1 is done="+str(var))
    # The value of id change indicating that a copy is given and not a sharing of var
    print (str(os.getpid())+": Value of id(x)="+str(id(var)))

    print (str(os.getpid())+": Done with main thread")
