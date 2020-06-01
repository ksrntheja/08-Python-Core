from threading import *

l = RLock()


def factorial(n):
    l.acquire()
    print('Lock acquired by', current_thread())
    if n < 1:
        result = 1
    else:
        result = n * factorial(n - 1)
    l.release()
    return result


def factorialResult(n):
    print("The Factorial of", n, "is:", factorial(n))


t1 = Thread(target=factorialResult, args=(5,))
t2 = Thread(target=factorialResult, args=(9,))
t1.start()
t2.start()

# Lock acquired by <Thread(Thread-1, started 140688022636288)>
# Lock acquired by <Thread(Thread-1, started 140688022636288)>
# Lock acquired by <Thread(Thread-1, started 140688022636288)>
# Lock acquired by <Thread(Thread-1, started 140688022636288)>
# Lock acquired by <Thread(Thread-1, started 140688022636288)>
# Lock acquired by <Thread(Thread-1, started 140688022636288)>
# The Factorial of 5 is: 120
# Lock acquired by <Thread(Thread-2, started 140688014243584)>
# Lock acquired by <Thread(Thread-2, started 140688014243584)>
# Lock acquired by <Thread(Thread-2, started 140688014243584)>
# Lock acquired by <Thread(Thread-2, started 140688014243584)>
# Lock acquired by <Thread(Thread-2, started 140688014243584)>
# Lock acquired by <Thread(Thread-2, started 140688014243584)>
# Lock acquired by <Thread(Thread-2, started 140688014243584)>
# Lock acquired by <Thread(Thread-2, started 140688014243584)>
# Lock acquired by <Thread(Thread-2, started 140688014243584)>
# Lock acquired by <Thread(Thread-2, started 140688014243584)>
# The Factorial of 9 is: 362880
