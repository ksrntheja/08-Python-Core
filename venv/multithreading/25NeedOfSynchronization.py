from threading import *
import time


def wish(name):
    for i in range(4):
        print('Good Evening from {}:'.format(current_thread().getName()), end='')
        time.sleep(2)
        print(name)


t1 = Thread(target=wish, args=('ksrn',))
t2 = Thread(target=wish, args=('theja',))
t1.start()
t2.start()

# Good Evening from Thread-1:Good Evening from Thread-2:ksrn
# Good Evening from Thread-1:theja
# Good Evening from Thread-2:ksrn
# Good Evening from Thread-1:theja
# Good Evening from Thread-2:theja
# Good Evening from Thread-2:ksrn
# Good Evening from Thread-1:theja
# ksrn
