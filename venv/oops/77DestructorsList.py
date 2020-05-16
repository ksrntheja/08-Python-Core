import time


class Test:
    def __init__(self):
        print("Constructor Execution...")

    def __del__(self):
        print("Destructor Execution...")


list = [Test(), Test(), Test()]
print('Deleting list')
del list
time.sleep(5)
print("End of application")

# Constructor Execution...
# Constructor Execution...
# Constructor Execution...
# Deleting list
# Destructor Execution...
# Destructor Execution...
# Destructor Execution...
# End of application
