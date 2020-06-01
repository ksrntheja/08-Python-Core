from threading import *

l = RLock()


def f01(n):
    l.acquire()
    print('Processing', n, current_thread().getName())
    if n < 1:
        return n
    return f01(n - 1) * n


f01(4)
print('End of main')

# Processing 4 MainThread
# Processing 3 MainThread
# Processing 2 MainThread
# Processing 1 MainThread
# Processing 0 MainThread
# End of main
