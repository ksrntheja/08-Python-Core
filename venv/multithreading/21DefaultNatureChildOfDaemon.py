from threading import *
import time


def job01():
    print(current_thread().getName(), 'is daemon', current_thread().isDaemon())
    t = Thread(target=job02)
    t.start()


def job02():
    print(current_thread().getName(), 'is daemon', current_thread().isDaemon())


t = Thread(target=job01)
print(t.isDaemon())
t.setDaemon(True)
t.start()
time.sleep(2)
print(current_thread(), 'end')

# False
# Thread-1 is daemon True
# Thread-2 is daemon True
# <_MainThread(MainThread, started 139927487063872)> end
