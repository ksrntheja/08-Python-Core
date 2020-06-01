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
doubles(numbers)
squares(numbers)
print("The total time taken:", time.time() - beginTime)

# Double: 2
# Double: 4
# Double: 6
# Double: 8
# Double: 10
# Double: 12
# Square: 1
# Square: 4
# Square: 9
# Square: 16
# Square: 25
# Square: 36
# The total time taken: 12.011766910552979
