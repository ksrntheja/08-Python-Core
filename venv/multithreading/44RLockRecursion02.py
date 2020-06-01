from threading import *

l = RLock()


def factorial(n):
    l.acquire()
    print('Lock acquired by', current_thread(), 'for', n)
    if n < 1:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result


def factorialResult(n):
    print("The Factorial of", n, "is:", factorial(n))


t1 = Thread(target=factorialResult, args=(5,))
t2 = Thread(target=factorialResult, args=(9,))
t1.start()
t2.start()
print('Main is releasing lock', l.release())

# Lock acquired by <Thread(Thread-1, started 140442794997504)> for 5
# Lock acquired by <Thread(Thread-1, started 140442794997504)> for 4
# Lock acquired by <Thread(Thread-1, started 140442794997504)> for 3
# Lock acquired by <Thread(Thread-1, started 140442794997504)> for 2
# Lock acquired by <Thread(Thread-1, started 140442794997504)> for 1
# Lock acquired by <Thread(Thread-1, started 140442794997504)> for 0
# The Factorial of 5 is: 120
# Traceback (most recent call last):
#   File "/Code/venv/multithreading/44RLockRecursion02.py", line <>, in <module>
#     print('Main is releasing lock', l.release())
# RuntimeError: cannot release un-acquired lock
# Exception ignored in: <module 'threading' from '/usr/lib/python3.6/threading.py'>
# Traceback (most recent call last):
#   File "/usr/lib/python3.6/threading.py", line 1294, in _shutdown
#     t.join()
#   File "/usr/lib/python3.6/threading.py", line 1056, in join
#     self._wait_for_tstate_lock()
#   File "/usr/lib/python3.6/threading.py", line 1072, in _wait_for_tstate_lock
#     elif lock.acquire(block, timeout):
# KeyboardInterrupt
