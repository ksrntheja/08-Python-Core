from threading import *
import time


def display():
    print(current_thread().getName(), "...started")
    time.sleep(3)
    print(current_thread().getName(), "...ended")


t1 = Thread(target=display, name="ChildThread1")
t2 = Thread(target=display, name="ChildThread2")
t1.start()
t2.start()

print(t1.name, "is Alive :", t1.isAlive())
print(t2.name, "is Alive :", t2.isAlive())
time.sleep(5)
print(t1.name, "is Alive :", t1.isAlive())
print(t2.name, "is Alive :", t2.isAlive())

# ChildThread1 ...started
# ChildThread2 ...started
# ChildThread1 is Alive : True
# ChildThread2 is Alive : True
# ChildThread1 ...ended
# ChildThread2 ...ended
# ChildThread1 is Alive : False
# ChildThread2 is Alive : False
