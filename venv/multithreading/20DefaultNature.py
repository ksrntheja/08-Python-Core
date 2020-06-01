from threading import *


def job():
    print("Child Thread")


t = Thread(target=job)
print(t.isDaemon())
t.setDaemon(True)
print(t.isDaemon())

# False
# True
