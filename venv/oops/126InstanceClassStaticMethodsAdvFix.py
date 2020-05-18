class P:

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

    @classmethod
    def method2(cls):
        super(C, cls).__init__(cls)
        super(C, cls).m1(cls)
        super().m2()
        super().m3()

    @staticmethod
    def method3():
        # super(C, C).__init__()
        # Traceback (most recent call last):
        #   File "/Code/venv/oops/126InstanceClassStaticMethodsAdvFix.py", line <>, in <module>
        #     c.method3()
        #   File "/Code/venv/oops/126InstanceClassStaticMethodsAdvFix.py", line <>, in method3
        #     super(C, C).__init__()
        # TypeError: __init__() missing 1 required positional argument: 'self'
        # super(C, C).m1()
        # Traceback (most recent call last):
        #   File "/Code/venv/oops/126InstanceClassStaticMethodsAdvFix.py", line <>, in <module>
        #     c.method3()
        #   File "/Code/venv/oops/126InstanceClassStaticMethodsAdvFix.py", line <>, in method3
        #     super(C, C).m1()
        # TypeError: m1() missing 1 required positional argument: 'self'
        super(C, C).m2()
        super(C, C).m3()


c = C()
print('Calling c.method2()')
c.method2()
print('Calling c.method3()')
c.method3()

# P constructor
# Calling c.method2()
# P constructor
# Parent instance method
# Parent class method
# Parent static method
# Calling c.method3()
# Parent class method
# Parent static method
