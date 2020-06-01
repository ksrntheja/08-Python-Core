from threading import *


class Test:
    def display(self):
        for i in range(10):
            print("Child Thread executed by:", current_thread().getName())


obj = Test()
t1 = Thread(target=obj.display)
t2 = Thread(target=obj.display)
t3 = Thread(target=obj.display)
t4 = Thread(target=obj.display)
t1.start()
t2.start()
t3.start()
t4.start()
for i in range(10):
    print("Main Thread-2")

# Child Thread executed by: Thread-1
# Child Thread executed by: Thread-1
# Child Thread executed by: Thread-1
# Child Thread executed by: Thread-1
# Child Thread executed by: Thread-2
# Child Thread executed by: Thread-1
# Child Thread executed by: Thread-1
# Child Thread executed by: Thread-1
# Child Thread executed by: Thread-1
# Child Thread executed by: Thread-1
# Child Thread executed by: Thread-1
# Child Thread executed by: Thread-2
# Child Thread executed by: Thread-3
# Child Thread executed by: Thread-3
# Child Thread executed by: Thread-3
# Child Thread executed by: Thread-3
# Child Thread executed by: Thread-3
# Child Thread executed by: Thread-2
# Child Thread executed by: Thread-2
# Child Thread executed by: Thread-2
# Child Thread executed by: Thread-2
# Child Thread executed by: Thread-2
# Child Thread executed by: Thread-2
# Child Thread executed by: Thread-2
# Child Thread executed by: Thread-2
# Child Thread executed by: Thread-3
# Child Thread executed by: Thread-4
# Child Thread executed by: Thread-3
# Child Thread executed by: Thread-3
# Child Thread executed by: Thread-3
# Child Thread executed by: Thread-3
# Child Thread executed by: Thread-4
# Child Thread executed by: Thread-4
# Child Thread executed by: Thread-4
# Child Thread executed by: Thread-4
# Child Thread executed by: Thread-4
# Child Thread executed by: Thread-4
# Main Thread-2
# Main Thread-2
# Main Thread-2
# Main Thread-2
# Main Thread-2
# Main Thread-2
# Main Thread-2
# Main Thread-2
# Main Thread-2
# Main Thread-2
# Child Thread executed by: Thread-4
# Child Thread executed by: Thread-4
# Child Thread executed by: Thread-4
