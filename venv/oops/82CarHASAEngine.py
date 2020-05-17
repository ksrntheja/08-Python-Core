class Engine:
    a = 10

    def __init__(self):
        self.b = 20

    def m(self):
        print('Engine Specific Functionality')


class Car:
    def __init__(self):
        self.engine = Engine()

    def m(self):
        print('Car using Engine Class Functionality')
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m()


c = Car()
c.m()

# Car using Engine Class Functionality
# 10
# 20
# Engine Specific Functionality
