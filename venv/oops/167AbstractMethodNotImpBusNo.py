class Vehicle:
    def __init__(self):
        print('Vehicle Constructor')

    def getNoOfWheels(self):
        pass


class Bus(Vehicle):
    pass


b = Bus()
print(b.getNoOfWheels())

# Vehicle Constructor
# None