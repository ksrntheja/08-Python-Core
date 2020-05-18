class A:
    # def m1(self):
    #     print('A class method')
    pass


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

# Traceback (most recent call last):
#   File "/Code/venv/oops/114MROFunctionMethodDemo.py", line <>, in <module>
#     d.m1()
# AttributeError: 'D' object has no attribute 'm1'
