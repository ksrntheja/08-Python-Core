from threading import *

l = RLock()

l.acquire()
l.release()
l.release()

# Traceback (most recent call last):
#   File "/Code/venv/multithreading/38ReentrantLockUnEqualAcquire.py", line <>, in <module>
#     l.release()
# RuntimeError: cannot release un-acquired lock
