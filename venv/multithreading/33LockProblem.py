from threading import *

l = Lock()
print("Main Thread trying to acquire Lock")
l.acquire()
print("Main Thread trying to acquire Lock Again")
l.acquire()

# Main Thread trying to acquire Lock
# Main Thread trying to acquire Lock Again
# Traceback (most recent call last):
#   File "/Code/venv/multithreading/33LockProblem.py", line <>, in <module>
#     l.acquire()
# KeyboardInterrupt
