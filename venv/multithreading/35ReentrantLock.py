from threading import *

l = RLock()
print("Main Thread trying to acquire Lock")
l.acquire()
print("Main Thread trying to acquire Lock Again")
l.acquire()

# Main Thread trying to acquire Lock
# Main Thread trying to acquire Lock Again
