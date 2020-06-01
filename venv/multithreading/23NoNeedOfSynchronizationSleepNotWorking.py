from threading import *
import time


def wish(name):
    for i in range(4):
        # print('Good Evening from {}:'.format(current_thread().getName()), end='')
        print('Good Evening from {}:'.format(current_thread().getName()), flush=True, end='')
        time.sleep(2)
        print(name)


wish('ksrntheja')

#         print('Good Evening from {}:'.format(current_thread().getName()), end='')
# Good Evening from MainThread:ksrntheja [Printed at a time]
# Good Evening from MainThread:ksrntheja
# Good Evening from MainThread:ksrntheja
# Good Evening from MainThread:ksrntheja

# Use flush = true
# Good Evening from MainThread:ksrntheja
# Good Evening from MainThread:

# total o/p:
# Good Evening from MainThread:ksrntheja
# Good Evening from MainThread:ksrntheja
# Good Evening from MainThread:ksrntheja
# Good Evening from MainThread:ksrntheja
