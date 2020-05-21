from abc import abstractmethod


class Vehicle:
    def __init__(self):
        print('Vehicle Constructor')

    @abstractmethod
    def getNoOfWheels(self):
        print('Hello')


v = Vehicle()
v.getNoOfWheels()

# Vehicle Constructor
# Hello
