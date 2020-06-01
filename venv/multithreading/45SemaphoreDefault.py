from threading import *
import time

s = Semaphore()


def wish(name):
    s.acquire()
    for i in range(4):
        print("Good Evening from {}:".format(current_thread().getName()), end='', flush=True)
        time.sleep(2)
        print(name)
    s.release()


t1 = Thread(target=wish, args=("t1",))
t2 = Thread(target=wish, args=("t2",))
t3 = Thread(target=wish, args=("t3",))
t4 = Thread(target=wish, args=("t4",))
t5 = Thread(target=wish, args=("t5",))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

# Good Evening from Thread-1:t1
# Good Evening from Thread-1:t1
# Good Evening from Thread-1:t1
# Good Evening from Thread-1:t1
# Good Evening from Thread-2:t2
# Good Evening from Thread-2:t2
# Good Evening from Thread-2:t2
# Good Evening from Thread-2:t2
# Good Evening from Thread-3:t3
# Good Evening from Thread-3:t3
# Good Evening from Thread-3:t3
# Good Evening from Thread-3:t3
# Good Evening from Thread-4:t4
# Good Evening from Thread-4:t4
# Good Evening from Thread-4:t4
# Good Evening from Thread-4:t4
# Good Evening from Thread-5:t5
# Good Evening from Thread-5:t5
# Good Evening from Thread-5:t5
# Good Evening from Thread-5:t5