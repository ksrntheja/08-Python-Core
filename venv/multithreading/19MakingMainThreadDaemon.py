from threading import *

print(current_thread().isDaemon())
current_thread().setDaemon(True)

# False
# Traceback (most recent call last):
#   File "/Code/venv/multithreading/19MakingMainThreadDaemon.py", line <>, in <module>
#     current_thread().setDaemon(True)
#   File "/usr/lib/python3.6/threading.py", line 1148, in setDaemon
#     self.daemon = daemonic
#   File "/usr/lib/python3.6/threading.py", line 1141, in daemon
#     raise RuntimeError("cannot set daemon status of active thread")
# RuntimeError: cannot set daemon status of active thread
