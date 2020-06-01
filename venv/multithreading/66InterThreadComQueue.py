from threading import *
import time
import random
import queue


def produce(q):
    while True:
        item = random.randint(1, 100)
        print("Producer Producing Item:", item)
        q.put(item)
        print("Producer giving Notification and sleeping", flush=True)
        time.sleep(5)
        print('Producer woke up', flush=True)


def consume(q):
    while True:
        print("Consumer waiting for updation")
        print("Consumer consumed the item:", q.get())
        print("Consumer sleeping", flush=True)
        time.sleep(5)
        print('Consumer woke up', flush=True)


q = queue.Queue()
t1 = Thread(target=consume, args=(q,))
t2 = Thread(target=produce, args=(q,))
t1.start()
t2.start()

# Consumer waiting for updation
# Producer Producing Item: 82
# Producer giving Notification and sleeping
# Consumer consumed the item: 82
# Consumer sleeping
# Consumer woke up
# Consumer waiting for updation
# Producer woke up
# Producer Producing Item: 32
# Producer giving Notification and sleeping
# Consumer consumed the item: 32
# Consumer sleeping
# -----------------------------------
# Producer woke up
# Producer Producing Item: 44
# Producer giving Notification and sleeping
# Consumer woke up
# Consumer waiting for updation
# Consumer consumed the item: 44
# Consumer sleeping
# Producer woke up
# Producer Producing Item: 45
# Producer giving Notification and sleeping
# Consumer woke up
# Consumer waiting for updation
# Consumer consumed the item: 45
# Consumer sleeping
# Consumer woke up
# Consumer waiting for updation
# Producer woke up
# Producer Producing Item: 68
# Producer giving Notification and sleeping
# Consumer consumed the item: 68
# Consumer sleeping
# Exception ignored in: <module 'threading' from '/usr/lib/python3.6/threading.py'>
# Traceback (most recent call last):
#   File "/usr/lib/python3.6/threading.py", line 1294, in _shutdown
#     t.join()
#   File "/usr/lib/python3.6/threading.py", line 1056, in join
#     self._wait_for_tstate_lock()
#   File "/usr/lib/python3.6/threading.py", line 1072, in _wait_for_tstate_lock
#     elif lock.acquire(block, timeout):
# KeyboardInterrupt
