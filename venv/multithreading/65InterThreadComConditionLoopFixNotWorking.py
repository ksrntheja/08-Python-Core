from threading import *
import time
import random

items = []


def produce(c):
    while True:
        c.acquire()
        item = random.randint(1, 100)
        print("Producer Producing Item:", item, flush=True)
        items.append(item)
        print("Producer giving Notification", flush=True)
        c.notify()
        print('Producer releasing and sleeping', flush=True)
        c.release()
        time.sleep(5)
        print('Producer woke up', flush=True)


def consume(c):
    while True:
        c.acquire()
        print("Consumer waiting for updation", flush=True)
        c.wait()
        print("Consumer consumed the item", items.pop(), flush=True)
        print('Consumer releasing and sleeping', flush=True)
        c.release()
        time.sleep(5)
        print('Consumer woke up', flush=True)


c = Condition()
t1 = Thread(target=consume, args=(c,))
t2 = Thread(target=produce, args=(c,))
t2.start()
t1.start()

# Producer Producing Item: 5
# Producer giving Notification
# Producer releasing and sleeping
# Consumer waiting for updation
# Producer woke up
# Producer Producing Item: 47
# Producer giving Notification
# Producer releasing and sleeping
# Consumer consumed the item 47
# Consumer releasing and sleeping
# Consumer woke up
# Consumer waiting for updation
# Producer woke up
# Producer Producing Item: 24
# Producer giving Notification
# Producer releasing and sleeping
# Consumer consumed the item 24
# Consumer releasing and sleeping
# Producer woke up
# Producer Producing Item: 36
# Producer giving Notification
# Consumer woke up
# Producer releasing and sleeping
# Consumer waiting for updation
# Producer woke up
# Producer Producing Item: 83
# Producer giving Notification
# Producer releasing and sleeping
# Consumer consumed the item 83
# Consumer releasing and sleeping
# Exception ignored in: <module 'threading' from '/usr/lib/python3.6/threading.py'>
# Traceback (most recent call last):
#   File "/usr/lib/python3.6/threading.py", line 1294, in _shutdown
#     t.join()
#   File "/usr/lib/python3.6/threading.py", line 1056, in join
#     self._wait_for_tstate_lock()
#   File "/usr/lib/python3.6/threading.py", line 1072, in _wait_for_tstate_lock
#     elif lock.acquire(block, timeout):
# KeyboardInterrupt
