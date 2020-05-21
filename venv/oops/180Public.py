class Test:
    def __init__(self):
        self.x = 10

    def m1(self):
        print('Public method')

    def m2(self):
        print(self.x)
        self.m1()


print('Within class')
t = Test()
t.m2()
print('Outside class')
print(t.x)
t.m1()

# Within class
# 10
# Public method
# Outside class
# 10
# Public method
