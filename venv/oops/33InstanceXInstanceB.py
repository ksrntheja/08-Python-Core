class Test:
    x = 10

    def __init__(self):
        self.y = 20


print('Test.x', Test.x)
# print('Test.y', Test.y)
# AttributeError: type object 'Test' has no attribute 'y'
t1 = Test()
t2 = Test()
print('t1:', t1.x, t1.y)
print('t2:', t2.x, t2.y)
t1.x = 888
t1.y = 999
print('t1:', t1.x, t1.y)
print('t2:', t2.x, t2.y)
print('Test.x', Test.x)
# print('Test.y', Test.y)
# AttributeError: type object 'Test' has no attribute 'y'


# Test.x 10
# t1: 10 20
# t2: 10 20
# t1: 888 999
# t2: 10 20
# Test.x 10
