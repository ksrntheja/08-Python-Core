from threading import *
import time


def producer(event):
    print("Producer thread producing items:")
    print("Producer thread giving notification by setting event")
    event.set()


def consumer(event):
    print('Consumer sleeping')
    time.sleep(3)
    print(t1.getName(), 'is active:', t1.isAlive())
    print("Consumer thread is waiting for updation")
    event.wait()
    print("Consumer thread got notification and consuming items")


event = Event()
t1 = Thread(target=producer, args=(event,))
t2 = Thread(target=consumer, args=(event,))
t2.start()
t1.start()

# Consumer sleeping
# Producer thread producing items:
# Producer thread giving notification by setting event
# Thread-1 is active: False
# Consumer thread is waiting for updation
# Consumer thread got notification and consuming items
