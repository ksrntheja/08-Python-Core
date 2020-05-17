class Engine:
    a = 10

    def __init__(self):
        self.b = 20

    def m(self):
        print('Engine Specific Functionality')


class Car:

    def m(self):
        print('Car using Engine Class STATIC Functionality')
        print(Engine.a)


c = Car()
c.m()

# Car using Engine Class STATIC Functionality
# 10
