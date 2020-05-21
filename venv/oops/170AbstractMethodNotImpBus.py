from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self):
        print('Vehicle Constructor')

    @abstractmethod
    def getNoOfWheels(self):
        print('Hello')


class Bus(Vehicle):
    pass


b = Bus()
print(b.getNoOfWheels())

# Traceback (most recent call last):
#   File "/Code/venv/oops/162AbstractMethodNotImpBus.py", line <>, in <module>
#     b = Bus()
# TypeError: Can't instantiate abstract class Bus with abstract methods getNoOfWheels