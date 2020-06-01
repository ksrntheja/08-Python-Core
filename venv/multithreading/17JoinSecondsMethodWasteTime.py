from threading import *
import time


def display():
    print(current_thread().name)
    print('Sleep of', current_thread().name, 'started at', time.time())
    time.sleep(5)
    print('Sleep of', current_thread().name, 'done at', time.time())


t = Thread(target=display)
t.start()
t.join(10)
print(current_thread().name, 'done at', time.time())

# Thread-1
# Sleep of Thread-1 started at 1590643883.1291125
# Sleep of Thread-1 done at 1590643888.1343775
# MainThread done at 1590643888.1344805
