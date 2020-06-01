from threading import *


def display():
    print('IN DISPLAY FUNCTION This code executed by Thread:', current_thread().getName())


print('This code executed by Thread:', current_thread().getName())
t = Thread(target=display)
#   MainThread creates child Thread Object
#   Child Thread Object is responsible to execute display method (job)
t.start()
#   MainThread starts ChildThread
print('This code executed by Thread:', current_thread().getName())

# This code executed by Thread: MainThread
# IN DISPLAY FUNCTION This code executed by Thread: Thread-1
# This code executed by Thread: MainThread
