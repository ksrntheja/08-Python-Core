from threading import *
import time


def wish(name):
    for i in range(4):
        print('Good Evening from {}:'.format(current_thread().getName()), end='')
        time.sleep(2)
        print(name)


# t = Thread(target=wish, args='ksrntheja')
# t = Thread(target=wish, args=('ksrntheja'))
# Exception in thread Thread-1:
# Traceback (most recent call last):
#   File "/usr/lib/python3.6/threading.py", line 916, in _bootstrap_inner
#     self.run()
#   File "/usr/lib/python3.6/threading.py", line 864, in run
#     self._target(*self._args, **self._kwargs)
# TypeError: wish() takes 1 positional argument but 9 were given

t = Thread(target=wish, args=('ksrntheja',))
t.start()

# Good Evening from Thread-1:ksrntheja
# Good Evening from Thread-1:ksrntheja
# Good Evening from Thread-1:ksrntheja
# Good Evening from Thread-1:ksrntheja
