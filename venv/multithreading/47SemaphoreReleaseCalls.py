from threading import *

s = Semaphore(2)
s.acquire()
s.acquire()
s.release()
s.release()
s.release()
s.release()
print('End')

# End
