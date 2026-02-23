import threading
import time

def task():
    print("Thread started")
    time.sleep(3)
    print("Thread finished")

t = threading.Thread(target = task)
t.start()
t.join()

def numbers():
    for i in range(5):
        print("Number",i)

def letters():
    for k in "ABCF":
        print("Letter", k)

t1 = threading.Thread(target=numbers)
t2 = threading.Thread(target=letters)
t1.start()
t2.start()

t1.join()
t2.join()