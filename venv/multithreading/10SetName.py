from threading import *


def run():
    print('IN run FUNCTION This code executed by Thread:', current_thread().getName())


print('current_thread().getName():', current_thread().getName())
current_thread().setName('ksrntheja')
print('current_thread().getName():', current_thread().getName())
current_thread().name = 'theja'
print('current_thread().getName():', current_thread().getName())
# t = Thread(name='thejaksrn')
# current_thread().getName(): MainThread
# current_thread().getName(): ksrntheja
# current_thread().getName(): theja
# End of App
t = Thread(name='thejaksrn', target=run)
t.start()
print('End of App')

# current_thread().getName(): MainThread
# current_thread().getName(): ksrntheja
# current_thread().getName(): theja
# IN run FUNCTION This code executed by Thread: thejaksrn
# End of App
