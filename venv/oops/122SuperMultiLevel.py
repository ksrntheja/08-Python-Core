class A:
    def m(self):
        print('A class Method')


class B(A):
    def m(self):
        print('B class Method')


class C(B):
    def m(self):
        print('C class Method')


class D(C):
    def m(self):
        print('D class Method')


class E(D):
    def m(self):
        print('In E class Method')
        print('Calling super().m()')
        super().m()
        print('Calling Particular parent method using classname.methodname(self)')
        print('A.m(self)')
        A.m(self)
        print('B.m(self)')
        B.m(self)
        print('C.m(self)')
        C.m(self)
        print('Calling Particular parent method using super(classname, self).methodname')
        print('super(D, self).m()')
        super(D, self).m()
        print('super(C, self).m()')
        super(C, self).m()
        print('super(B, self).m()')
        super(B, self).m()
        print('super(A, self).m()')
        # super(A, self).m()
        #         Traceback (most recent call last):
        #   File "/Code/venv/oops/122SuperMultiLevel.py", line <>, in <module>
        #     e.m()
        #   File "/Code/venv/oops/122SuperMultiLevel.py", line <>, in m
        #     super(A, self).m()
        # AttributeError: 'super' object has no attribute 'm'


e = E()
e.m()

# In E class Method
# Calling super().m()
# D class Method
# Calling Particular parent method using classname.methodname(self)
# A.m(self)
# A class Method
# B.m(self)
# B class Method
# C.m(self)
# C class Method
# Calling Particular parent method using super(classname, self).methodname
# super(D, self).m()
# C class Method
# super(C, self).m()
# B class Method
# super(B, self).m()
# A class Method
# super(A, self).m()
