class P:
    a = 10

    def __init__(self):
        print('P constructor')
        self.b = 10


class C(P):

    def method(self):
        print('Using self to access parent members')
        print(self.a)
        print(self.b)
        print('Using super() to access parent members')
        print(super().a)
        # print(super().b)
        # Traceback (most recent call last):
        #   File "/Code/venv/oops/122SuperInstanceVariables.py", line <>, in <module>
        #     c.method()
        #   File "/Code/venv/oops/122SuperInstanceVariables.py", line <>, in method
        #     print(super().b)
        # AttributeError: 'super' object has no attribute 'b'


c = C()
c.method()

# C constructor
# P constructor
# Calling parent members with super()
# 10
# Parent instance method
# Parent class method
# Parent static method
# Calling current members with self
# 888
# 10
