from threading import *
import time


def producer():
    print('Producer sleeping')
    time.sleep(5)
    print("Producer thread producing items:")
    print("Producer thread giving notification by setting event")
    event.set()


def consumer():
    print("Consumer thread is waiting for updation")
    event.wait()
    print("Consumer thread got notification and consuming items")


event = Event()
t1 = Thread(target=producer)
t2 = Thread(target=consumer)
t1.start()
t2.start()
print(current_thread().getName(), 'started ', t1.getName(), '&', t2.getName())
for i in range(6):
    print(t1.name, ' is active:', t1.isAlive())
    print(t2.name, ' is active:', t2.isAlive())
    time.sleep(1)

# Producer sleeping
# Consumer thread is waiting for updation
# MainThread started  Thread-1 & Thread-2
# Thread-1  is active: True
# Thread-2  is active: True
# Thread-1  is active: True
# Thread-2  is active: True
# Thread-1  is active: True
# Thread-2  is active: True
# Thread-1  is active: True
# Thread-2  is active: True
# Thread-1  is active: True
# Thread-2  is active: True
# Producer thread producing items:
# Producer thread giving notification by setting event
# Consumer thread got notification and consuming items
# Thread-1  is active: False
# Thread-2  is active: False
