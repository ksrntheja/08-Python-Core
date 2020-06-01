from threading import *


def test():
    print("Child Thread:", current_thread().ident)


t = Thread(target=test)
t.start()
print("Main Thread Identification Number:", current_thread().ident)
print("Child Thread Identification Number:", t.ident)

# Child Thread: 140163358742272
# Main Thread Identification Number: 140163391354688
# Child Thread Identification Number: 140163358742272
