from threading import *

l = Lock()


def f01(n):
    l.acquire()
    print('Processing', n, current_thread().getName())
    result = f01(n - 1) * n


f01(10)
print('End of main')

# Processing 10 MainThread
# Traceback (most recent call last):
#   File "/Code/venv/multithreading/34LockProblemRecursion.py", line <>, in <module>
#     f01(10)
#   File "/Code/venv/multithreading/34LockProblemRecursion.py", line <>, in f01
#     result = f01(n - 1) * n
#   File "/Code/venv/multithreading/34LockProblemRecursion.py", line <>, in f01
#     l.acquire()
# KeyboardInterrupt
