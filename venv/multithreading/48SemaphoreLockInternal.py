from threading import *

s = Semaphore()
s.acquire()
s.acquire()
print('End')

# Traceback (most recent call last):
#   File "/Code/venv/multithreading/48SemaphoreLockInternal.py", line <>, in <module>
#     s.acquire()
#   File "/usr/lib/python3.6/threading.py", line 426, in acquire
#     self._cond.wait(timeout)
#   File "/usr/lib/python3.6/threading.py", line 295, in wait
#     waiter.acquire()
# KeyboardInterrupt