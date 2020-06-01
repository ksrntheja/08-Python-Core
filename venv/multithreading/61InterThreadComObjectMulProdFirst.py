from threading import *
import time


def producer(condition):
    condition.acquire()
    print("Producer thread producing items:")
    print("Producer thread giving notification by setting event")
    condition.notify()
    print("Notified")
    condition.release()


def consumer(condition):
    condition.acquire()
    print("Consumer thread is waiting for updation", current_thread().getName())
    condition.wait()
    print("Consumer thread got notification and consuming items", current_thread().getName())
    condition.release()


condition = Condition()
t1 = Thread(target=producer, name='producer', args=(condition,))
t2 = Thread(target=consumer, args=(condition,))
t3 = Thread(target=consumer, args=(condition,))
t1.start()
t2.start()
t3.start()
time.sleep(2)
print(t1.isAlive())
print(t2.isAlive())
print(t3.isAlive())

# Producer thread producing items:
# Producer thread giving notification by setting event
# Notified
# Consumer thread is waiting for updation Thread-1
# Consumer thread is waiting for updation Thread-2
# False
# True
# True
# Exception ignored in: <module 'threading' from '/usr/lib/python3.6/threading.py'>
# Traceback (most recent call last):
#   File "/usr/lib/python3.6/threading.py", line 1294, in _shutdown
#     t.join()
#   File "/usr/lib/python3.6/threading.py", line 1056, in join
#     self._wait_for_tstate_lock()
#   File "/usr/lib/python3.6/threading.py", line 1072, in _wait_for_tstate_lock
#     elif lock.acquire(block, timeout):
# KeyboardInterrupt
