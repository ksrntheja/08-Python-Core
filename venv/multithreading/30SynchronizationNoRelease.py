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

# Good Evening from Thread-1:ksrn
# Good Evening from Thread-1:ksrn
# Good Evening from Thread-1:ksrn
# Good Evening from Thread-1:ksrn
# Exception ignored in: <module 'threading' from '/usr/lib/python3.6/threading.py'>
# Traceback (most recent call last):
#   File "/usr/lib/python3.6/threading.py", line 1294, in _shutdown
#     t.join()
#   File "/usr/lib/python3.6/threading.py", line 1056, in join
#     self._wait_for_tstate_lock()
#   File "/usr/lib/python3.6/threading.py", line 1072, in _wait_for_tstate_lock
#     elif lock.acquire(block, timeout):
# KeyboardInterrupt
