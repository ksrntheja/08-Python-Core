class Test:
    def m1(self):
        print('no-arg method')

    def m1(self, a):
        print('one-arg method')

    def m1(self, a, b):
        print('two-arg method')


t = Test()
# t.m1()
# Traceback (most recent call last):
#   File "/Code/venv/oops/139MethodOverloadingVariableLengthArgv.py", line <>, in <module>
#     t.m1()
# TypeError: m1() missing 2 required positional arguments: 'a' and 'b'
# t.m1(10)
# Traceback (most recent call last):
#   File "/Code/venv/oops/139MethodOverloadingVariableLengthArgv.py", line <>, in <module>
#     t.m1(10)
# TypeError: m1() missing 1 required positional argument: 'b'
t.m1(10, 20)

# two-arg method
