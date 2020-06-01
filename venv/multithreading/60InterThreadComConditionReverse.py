from threading import *


def consume(c):
    c.acquire()
    print("Consumer waiting for updation")
    c.wait()
    print("Consumer got notification & consuming the item")
    c.release()


def produce(c):
    c.acquire()
    print("Producer Producing Items")
    print("Producer giving Notification")
    c.notify()
    c.release()


c = Condition()
t1 = Thread(target=consume, args=(c,))
t2 = Thread(target=produce, args=(c,))
t2.start()
t1.start()

# Producer Producing Items
# Producer giving Notification
# Consumer waiting for updation
# Exception ignored in: <module 'threading' from '/usr/lib/python3.6/threading.py'>
# Traceback (most recent call last):
#   File "/usr/lib/python3.6/threading.py", line 1294, in _shutdown
#     t.join()
#   File "/usr/lib/python3.6/threading.py", line 1056, in join
#     self._wait_for_tstate_lock()
#   File "/usr/lib/python3.6/threading.py", line 1072, in _wait_for_tstate_lock
#     elif lock.acquire(block, timeout):
# KeyboardInterrupt
