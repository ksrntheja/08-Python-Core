from threading import *

l = Lock()


def factorial(n):
    l.acquire()
    print('Lock acquired by', current_thread())
    if n < 1:
        result = 1
    else:
        result = n * factorial(n - 1)
    l.release()
    return result


def factorialResult(n):
    print("The Factorial of", n, "is:", factorial(n))


t1 = Thread(target=factorialResult, args=(5,))
t2 = Thread(target=factorialResult, args=(9,))
t1.start()
t2.start()

# Lock acquired by <Thread(Thread-1, started 140701309003520)>
# Exception ignored in: <module 'threading' from '/usr/lib/python3.6/threading.py'>
# Traceback (most recent call last):
#   File "/usr/lib/python3.6/threading.py", line 1294, in _shutdown
#     t.join()
#   File "/usr/lib/python3.6/threading.py", line 1056, in join
#     self._wait_for_tstate_lock()
#   File "/usr/lib/python3.6/threading.py", line 1072, in _wait_for_tstate_lock
#     elif lock.acquire(block, timeout):
# KeyboardInterrupt
