import multiprocessing
import os

var = 100

def print_square(num):
    print str(os.getpid())+": Sqaure is: "+str(num*num)
    global var
    var = 20
    print (str(os.getpid())+": Value of global var when changed in process ="+str(var))
    print (str(os.getpid())+": Value of id(x)="+str(id(var)))

def print_cube(num):
    print str(os.getpid())+": Cube is: "+str(num*num*num)

if __name__ == '__main__':
    # Create processes
    print (str(os.getpid())+": Var in main before spawing process="+str(var))
    print (str(os.getpid())+": Value of id(x)="+str(id(var)))
    p1 = multiprocessing.Process(target=print_square, args=(10,))
    p2 = multiprocessing.Process(target=print_cube, args=(9,))
    
    # Start the process
    p1.start()
    p2.start()
    
    # Wait for processes to complete before main process exits
    p1.join()
    p2.join()

    # Process p1 changes the global variable. Let's check if it is reflected here after p1 is done with it's work
    # Parent process does a deep copy and hence there will be no change in value of var as child has it's own copy of var
    print (str(os.getpid())+": Var in main after p1 is done="+str(var))
    # The value of id change indicating that a copy is given and not a sharing of var
    print (str(os.getpid())+": Value of id(x)="+str(id(var)))

    print (str(os.getpid())+": Done with main thread")
