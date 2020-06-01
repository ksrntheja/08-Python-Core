from threading import *
import time


def producer(condition):
    condition.acquire()
    print("Producer thread producing items:")
    print("Producer thread giving notification by setting event")
    condition.notifyAll()
    print("Notified All")
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
t2.start()
t3.start()
t1.start()
time.sleep(2)
print(t1.isAlive())
print(t2.isAlive())
print(t3.isAlive())

# Consumer thread is waiting for updation Thread-1
# Consumer thread is waiting for updation Thread-2
# Producer thread producing items:
# Producer thread giving notification by setting event
# Notified All
# Consumer thread got notification and consuming items Thread-1
# Consumer thread got notification and consuming items Thread-2
# False
# False
# False
