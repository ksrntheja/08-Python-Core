from abc import abstractmethod


class Vehicle:
    def __init__(self):
        print('Vehicle Constructor')

    @abstractmethod
    def getNoOfWheels(self):
        pass


v = Vehicle()

# Vehicle Constructor
