from threading import *
import time

l = Lock()


def wish(name):
    l.acquire()
    try:
        for i in range(10):
            print("Good Evening:", end='')
            time.sleep(2)
            print(name)
    finally:
        l.release()


t1 = Thread(target=wish, args=("ksrn",))
t2 = Thread(target=wish, args=("theja",))
t3 = Thread(target=wish, args=("ajeht",))
t1.start()
t2.start()
t3.start()

# Good Evening:ksrn
# Good Evening:ksrn
# Good Evening:ksrn
# Good Evening:ksrn
# Good Evening:ksrn
# Good Evening:ksrn
# Good Evening:ksrn
# Good Evening:ksrn
# Good Evening:ksrn
# Good Evening:ksrn
# Good Evening:theja
# Good Evening:theja
# Good Evening:theja
# Good Evening:theja
# Good Evening:theja
# Good Evening:theja
# Good Evening:theja
# Good Evening:theja
# Good Evening:theja
# Good Evening:theja
# Good Evening:ajeht
# Good Evening:ajeht
# Good Evening:ajeht
# Good Evening:ajeht
# Good Evening:ajeht
# Good Evening:ajeht
# Good Evening:ajeht
# Good Evening:ajeht
# Good Evening:ajeht
# Good Evening:ajeht
