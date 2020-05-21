from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self):
        print('Vehicle Constructor')

    @abstractmethod
    def getNoOfWheels(self):
        print('Hello')


class Bus(Vehicle):

    def getNoOfWheels(self):
        return 7


class Auto(Vehicle):

    def getNoOfWheels(self):
        return 3


v = Vehicle()
v.getNoOfWheels()

# Traceback (most recent call last):
#   File "/Code/venv/oops/176AbstractMethodImpBusAutoError.py", line <>, in <module>
#     v = Vehicle()
# TypeError: Can't instantiate abstract class Vehicle with abstract methods getNoOfWheels
