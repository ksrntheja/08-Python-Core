from threading import *


def producer():
    print("Producer thread producing items:")
    print("Producer thread giving notification by setting event")
    event.set()


def consumer():
    print("Consumer thread is waiting for updation, producer isAlive:", t1.isAlive())
    event.wait()
    print("Consumer thread got notification and consuming items")


event = Event()
t1 = Thread(target=producer)
t2 = Thread(target=consumer)
t1.start()
t2.start()

# Producer thread producing items:
# Producer thread giving notification by setting event
# Consumer thread is waiting for updation, producer isAlive: False
# Consumer thread got notification and consuming items
