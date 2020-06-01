from threading import *

l = RLock()

l.acquire()
l.acquire()
l.release()

#
