from threading import *
import time


def display():
    for i in range(10):
        print(current_thread().name)
        time.sleep(2)


t = Thread(target=display)
t.start()
t.join(5)  # This Line executed by Main Thread
for i in range(10):
    print(current_thread().name)

# Thread-1
# Thread-1
# Thread-1
# MainThread
# MainThread
# MainThread
# MainThread
# MainThread
# MainThread
# MainThread
# MainThread
# MainThread
# MainThread
# Thread-1
# Thread-1
# Thread-1
# Thread-1
# Thread-1
# Thread-1
# Thread-1
