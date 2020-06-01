from threading import *
import time


def display():
    print(current_thread().getName(), "...started")
    time.sleep(3)
    print(current_thread().getName(), "...ended")


print("The Number of active Threads:", active_count())
t1 = Thread(target=display, name="ChildThread1")
t2 = Thread(target=display, name="ChildThread2")
t3 = Thread(target=display, name="ChildThread3")
t1.start()
t2.start()
t3.start()
print("The Number of active Threads:", active_count())
time.sleep(5)
print("The Number of active Threads:", active_count())

# The Number of active Threads: 1
# ChildThread1 ...started
# ChildThread2 ...started
# ChildThread3 ...started
# The Number of active Threads: 4
# ChildThread3 ...ended
# ChildThread1 ...ended
# ChildThread2 ...ended
# The Number of active Threads: 1
