from threading import *
import time

l = Lock()


def wish(name):
    l.acquire()
    for i in range(4):
        print('Good Evening from {}:'.format(current_thread().getName()), end='')
        time.sleep(2)
        print(name)
    # l.release()


t1 = Thread(target=wish, args=('ksrn',))
t2 = Thread(target=wish, args=('theja',))
t1.start()
t2.start()
time.sleep(10)
print("MainThead won't require the lock")
print('In', current_thread().name, 'check t1 isAlive :', t1.isAlive())
print('In', current_thread().name, 'check t2 isAlive :', t2.isAlive())

# Good Evening from Thread-1:ksrn
# Good Evening from Thread-1:ksrn
# Good Evening from Thread-1:ksrn
# Good Evening from Thread-1:ksrn
# In MainThread check t1 isAlive : False
# In MainThread check t2 isAlive : True
