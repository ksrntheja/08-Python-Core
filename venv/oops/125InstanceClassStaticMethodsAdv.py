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
    def __init__(self):
        print('C constructor')
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

    def method1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

    @classmethod
    def method2(cls):
        # super().__init__()
        # Traceback (most recent call last):
        #   File "/Code/venv/oops/125InstanceClassStaticMethodsAdv.py", line <>, in <module>
        #     c.method2()
        #   File "/Code/venv/oops/125InstanceClassStaticMethodsAdv.py", line <>, in method2
        #     super().__init__()
        # TypeError: __init__() missing 1 required positional argument: 'self'
        # super().m1()
        # Traceback (most recent call last):
        #   File "/Code/venv/oops/125InstanceClassStaticMethodsAdv.py", line <>, in <module>
        #     c.method2()
        #   File "/Code/venv/oops/125InstanceClassStaticMethodsAdv.py", line <>, in method2
        #     super().m1()
        # TypeError: m1() missing 1 required positional argument: 'self'
        super().m2()
        super().m3()

    @staticmethod
    def method3():
        # super().__init__()
        # Traceback (most recent call last):
        #   File "/Code/venv/oops/125InstanceClassStaticMethodsAdv.py", line <>, in <module>
        #     c.method3()
        #   File "/Code/venv/oops/125InstanceClassStaticMethodsAdv.py", line <>, in method3
        #     super().__init__()
        # RuntimeError: super(): no arguments
        # super().m1()
        # Traceback (most recent call last):
        #   File "/Code/venv/oops/125InstanceClassStaticMethodsAdv.py", line <>, in <module>
        #     c.method3()
        #   File "/Code/venv/oops/125InstanceClassStaticMethodsAdv.py", line <>, in method3
        #     super().m1()
        # RuntimeError: super(): no arguments
        # super().m2()
        # Traceback (most recent call last):
        #   File "/Code/venv/oops/125InstanceClassStaticMethodsAdv.py", line <>, in <module>
        #     c.method3()
        #   File "/Code/venv/oops/125InstanceClassStaticMethodsAdv.py", line <>, in method3
        #     super().m2()
        # RuntimeError: super(): no arguments
        # super().m3()
        #         Traceback (most recent call last):
        #   File "/Code/venv/oops/125InstanceClassStaticMethodsAdv.py", line <>, in <module>
        #     c.method3()
        #   File "/Code/venv/oops/125InstanceClassStaticMethodsAdv.py", line <>, in method3
        #     super().m3()
        # RuntimeError: super(): no arguments
        pass


c = C()
print('Calling c.method1()')
c.method1()
print('Calling c.method2()')
c.method2()
print('Calling c.method3()')
c.method3()

# C constructor
# P constructor
# Parent instance method
# Parent class method
# Parent static method
# Calling c.method1()
# P constructor
# Parent instance method
# Parent class method
# Parent static method
# Calling c.method2()
# Parent class method
# Parent static method
# Calling c.method3()
