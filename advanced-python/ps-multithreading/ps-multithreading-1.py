import threading
from time import sleep
from random import random

def worker(delay):
    """thread function"""
    t_name = threading.current_thread().getName()
    t_id = threading.current_thread().ident

    print(t_name, "waiting for", delay, "secs")
    sleep(delay)
    # Critical section of the code
    print (t_name, ":", t_id)

def main():
    """main thread"""

    list_of_child_thread = list()
    for item in range(5):
        # if we write it as target=worker() the mian thread will directly call worker function and
        # hence you see only main thread in o/p
        # Here a reference of target function is stored and once t.start() is called, the referred function is called
        # Value for target can be reference to a function or reference to method of a class or a class itself.
        random_value = random()
        t = threading.Thread(target=worker, args=(random_value,), name='Bhagyesh-'+str(item))
        list_of_child_thread.append(t)
        t.start()

    # Wait for each child thread to complete before main thread exists
    for t in list_of_child_thread:
        t.join()

    print ('Main thread exiting...')

if __name__ == '__main__':
    main()
