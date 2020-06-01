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
t1.start()
t2.start()

# Consumer waiting for updation
# Producer Producing Items
# Producer giving Notification
# Consumer got notification & consuming the item
