class P:
    a = 10

    def __init__(self):
        print('Parent constructor')
        self.b = 20

    def m01(self):
        print('Parent instance method')

    @classmethod
    def m02(cls):
        print('Parent class method')

    @staticmethod
    def m03():
        print('Parent static method')


class C(P):
    pass


c = C()
print(c.a)
print(c.b)
c.m01()
c.m02()
c.m03()
print('Accessing with C')
# C.m01()
# TypeError: m01() missing 1 required positional argument: 'self'
C.m02()
C.m03()

# Parent constructor
# 10
# 20
# Parent instance method
# Parent class method
# Parent static method
# Accessing with C
# Parent class method
# Parent static method
