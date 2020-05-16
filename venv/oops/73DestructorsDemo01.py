import time


class Test:
    def __init__(self):
        print("Object Initialization...")

    def __del__(self):
        print("Fulfilling Last Wish and performing clean up activities...")


t = Test()
print('Created Test Object')
t = None
print('Made "t" to point to None')
time.sleep(5)
print("End of application")

# Object Initialization...
# Created Test Object
# Fulfilling Last Wish and performing clean up activities...
# Made "t" to point to None
# End of application
