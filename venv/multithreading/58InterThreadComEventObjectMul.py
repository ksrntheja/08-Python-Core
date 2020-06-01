from threading import *


def producer():
    print("Producer thread producing items:")
    print("Producer thread giving notification by setting event")
    event.set()


def consumer():
    print("Consumer", current_thread().getName(), "is waiting for updation")
    event.wait()
    print("Consumer thread got notification and consuming items", current_thread().getName())


event = Event()
t1 = Thread(target=producer, name='producer')
t2 = Thread(target=consumer)
t3 = Thread(target=consumer)
t2.start()
t3.start()
t1.start()

# Consumer Thread-1 is waiting for updation
# Consumer Thread-2 is waiting for updation
# Producer thread producing items:
# Producer thread giving notification by setting event
# Consumer thread got notification and consuming items Thread-2
# Consumer thread got notification and consuming items Thread-1
