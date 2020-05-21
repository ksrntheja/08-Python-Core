from abc import ABC


class Vehicle(ABC):
    def __init__(self):
        print('Vehicle Constructor')

    # @abstractmethod
    def getNoOfWheels(self):
        pass


v = Vehicle()

# Vehicle Constructor
