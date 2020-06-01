from threading import *
import time

l = Lock()


def wish(name):
    l.acquire()
    for i in range(4):
        print('Good Evening from {}:'.format(current_thread().getName()), end='')
        time.sleep(2)
        print(name)
    l.release()


t1 = Thread(target=wish, args=('ksrn',))
t2 = Thread(target=wish, args=('theja',))
t1.start()
t2.start()
print("MainThead won't require the lock")
for i in range(20):
    print(i, current_thread().name, 'check t1 isAlive :', t1.isAlive())
    print(i, current_thread().name, 'check t2 isAlive :', t2.isAlive())
    time.sleep(1)

# /usr/bin/python3.6 //Code/venv/multithreading/32SynchronizationNoReleaseIsAliveAdv.py
# Good Evening from Thread-1:MainThead won't require the lock
# 0 MainThread check t1 isAlive : True
# 0 MainThread check t2 isAlive : True
# 1 MainThread check t1 isAlive : True
# 1 MainThread check t2 isAlive : True
# ksrn
# Good Evening from Thread-1:2 MainThread check t1 isAlive : True
# 2 MainThread check t2 isAlive : True
# 3 MainThread check t1 isAlive : True
# 3 MainThread check t2 isAlive : True
# ksrn
# Good Evening from Thread-1:4 MainThread check t1 isAlive : True
# 4 MainThread check t2 isAlive : True
# 5 MainThread check t1 isAlive : True
# 5 MainThread check t2 isAlive : True
# ksrn
# Good Evening from Thread-1:6 MainThread check t1 isAlive : True
# 6 MainThread check t2 isAlive : True
# 7 MainThread check t1 isAlive : True
# 7 MainThread check t2 isAlive : True
# ksrn
# Good Evening from Thread-2:8 MainThread check t1 isAlive : False
# 8 MainThread check t2 isAlive : True
# 9 MainThread check t1 isAlive : False
# 9 MainThread check t2 isAlive : True
# theja
# Good Evening from Thread-2:10 MainThread check t1 isAlive : False
# 10 MainThread check t2 isAlive : True
# 11 MainThread check t1 isAlive : False
# 11 MainThread check t2 isAlive : True
# theja
# Good Evening from Thread-2:12 MainThread check t1 isAlive : False
# 12 MainThread check t2 isAlive : True
# 13 MainThread check t1 isAlive : False
# 13 MainThread check t2 isAlive : True
# theja
# Good Evening from Thread-2:14 MainThread check t1 isAlive : False
# 14 MainThread check t2 isAlive : True
# 15 MainThread check t1 isAlive : False
# 15 MainThread check t2 isAlive : True
# theja
# 16 MainThread check t1 isAlive : False
# 16 MainThread check t2 isAlive : False
# 17 MainThread check t1 isAlive : False
# 17 MainThread check t2 isAlive : False
# 18 MainThread check t1 isAlive : False
# 18 MainThread check t2 isAlive : False
# 19 MainThread check t1 isAlive : False
# 19 MainThread check t2 isAlive : False
#
# Process finished with exit code 0
