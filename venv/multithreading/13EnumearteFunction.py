from threading import *
import time


def display():
    print(current_thread().getName(), "...started")
    time.sleep(3)
    print(current_thread().getName(), "...ended")


t1 = Thread(target=display, name="ChildThread1")
t2 = Thread(target=display, name="ChildThread2")
t3 = Thread(target=display, name="ChildThread3")
t1.start()
t2.start()
t3.start()

l = enumerate()
for t in l:
    print("Thread Name:", t.name)
time.sleep(5)
l = enumerate()
for t in l:
    print("Thread Name:", t.name)

# ChildThread1 ...started
# ChildThread2 ...started
# ChildThread3 ...started
# Thread Name: MainThread
# Thread Name: ChildThread1
# Thread Name: ChildThread2
# Thread Name: ChildThread3
# ChildThread3 ...ended
# ChildThread1 ...ended
# ChildThread2 ...ended
# Thread Name: MainThread
