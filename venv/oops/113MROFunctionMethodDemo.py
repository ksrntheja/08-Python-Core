class A:
    def m1(self):
        print('A class method')


class B(A):
    # def m1(self):
    #     print('B class method')
    pass


class C(A):
    # def m1(self):
    #     print('C class method')
    pass


class D(B, C):
    # def m1(self):
    #     print('D class method')
    pass


d = D()
d.m1()

# A class method
