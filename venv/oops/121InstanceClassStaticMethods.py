class P:
    a = 10

    def __init__(self):
        print('P constructor')

    def m1(self):
        print('Parent instance method')

    @classmethod
    def m2(cls):
        print('Parent class method')

    @staticmethod
    def m3():
        print('Parent static method')


class C(P):
    def __init__(self):
        print('C constructor')

    def method1(self):
        print('Calling parent members with super()')
        print(super().a)
        super().m1()
        super().m2()
        super().m3()
        super().__init__()
        print('Calling parent members with self')
        print(self.a)
        self.m1()
        self.m2()
        self.m3()
        self.__init__()


c = C()
c.method1()

# C constructor
# Calling parent members with super()
# 10
# Parent instance method
# Parent class method
# Parent static method
# P constructor
# Calling parent members with self
# 10
# Parent instance method
# Parent class method
# Parent static method
# C constructor
