from threading import *

import time


def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("Double:", 2 * n)


def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print("Square:", n * n)


numbers = [1, 2, 3, 4, 5, 6]
beginTime = time.time()
t1 = Thread(target=doubles, args=(numbers,))
t2 = Thread(target=squares, args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
print("The total time taken:", time.time() - beginTime)

# Double: 2
# Square: 1
# Double: 4
# Square: 4
# Square: 9
# Double: 6
# Square: 16
# Double: 8
# Square: 25
# Double: 10
# Square: 36
# Double: 12
# The total time taken: 6.006749153137207
