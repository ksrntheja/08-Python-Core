from threading import *

l = Lock()
# l.acquire()
l.release()

# Traceback (most recent call last):
#   File "/Code/venv/multithreading/27LockReleaseNoAcquire.py", line <>, in <module>
#     l.release()
# RuntimeError: release unlocked lock
