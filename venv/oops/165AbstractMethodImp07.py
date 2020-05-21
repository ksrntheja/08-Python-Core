from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self):
        print('Vehicle Constructor')

    @abstractmethod
    def getNoOfWheels(self):
        print('Hello')


v = Vehicle()
v.getNoOfWheels()

# Traceback (most recent call last):
#   File "/Code/venv/oops/160AbstractMethodImp2.py", line <>, in <module>
#     v = Vehicle()
# TypeError: Can't instantiate abstract class Vehicle with abstract methods getNoOfWheels
