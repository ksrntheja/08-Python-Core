from threading import *

l = Lock()
l.acquire()
l.release()
l.release()

# Traceback (most recent call last):
#   File "/Code/venv/multithreading/49LockAcquire2Release.py", line <>, in <module>
#     l.release()
# RuntimeError: release unlocked lock
