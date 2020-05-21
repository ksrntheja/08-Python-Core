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


b = Bus()
print(b.getNoOfWheels())
a = Auto()
print(a.getNoOfWheels())

# Vehicle Constructor
# 7
# Vehicle Constructor
# 3
