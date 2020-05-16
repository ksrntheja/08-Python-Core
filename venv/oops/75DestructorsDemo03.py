class Test:
    def __init__(self):
        print("Object Initialization...")

    def __del__(self):
        print("Fulfilling Last Wish and performing clean up activities...")


t1 = Test()
print('Created Test Object t1')
t2 = Test()
print('Created Test Object t2')
print("End of application")

# Object Initialization...
# Created Test Object t1
# Object Initialization...
# Created Test Object t2
# End of application
# Fulfilling Last Wish and performing clean up activities...
# Fulfilling Last Wish and performing clean up activities...
