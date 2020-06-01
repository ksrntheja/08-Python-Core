from threading import *

s = BoundedSemaphore(2)
s.acquire()
s.acquire()
s.release()
s.release()
s.release()
s.release()
print('End')

# Traceback (most recent call last):
#   File "/Code/venv/multithreading/51BoundedSemaphoreReleaseCalls.py", line <>, in <module>
#     s.release()
#   File "/usr/lib/python3.6/threading.py", line 482, in release
#     raise ValueError("Semaphore released too many times")
# ValueError: Semaphore released too many times
