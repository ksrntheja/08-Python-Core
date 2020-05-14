class Test:
    x = 10

    def __init__(self):
        self.y = 20

    @classmethod
    def m01(cls):
        cls.x = 888
        cls.y = 999


print('Test.x', Test.x)
# print('Test.y', Test.y)
# AttributeError: type object 'Test' has no attribute 'y'
t1 = Test()
t2 = Test()
print('t1:', t1.x, t1.y)
print('t2:', t2.x, t2.y)
t1.m01()
print('t1:', t1.x, t1.y)
print('t2:', t2.x, t2.y)
print('Test.x', Test.x)
print('Test.y', Test.y)

# Test.x 10
# t1: 10 20
# t2: 10 20
# t1: 888 20
# t2: 888 20
# Test.x 888
# Test.y 999
