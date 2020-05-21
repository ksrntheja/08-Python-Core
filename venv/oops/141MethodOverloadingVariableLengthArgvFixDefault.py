class Test:
    def m1(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            print('three-arg method')
        elif a is not None and b is not None:
            print('two-arg method')
        elif a is not None:
            print('one-arg method')
        else:
            print('No-arg method')


t = Test()
t.m1()
t.m1(10)
t.m1(10, 20)
t.m1(10, 20, 30)
t.m1(10, 20, 30, 40)

# No-arg method
# one-arg method
# two-arg method
# three-arg method
# Traceback (most recent call last):
#   File "/Code/venv/oops/141MethodOverloadingVariableLengthArgvFixDefault.py", line <>, in <module>
#     t.m1(10, 20, 30, 40)
# TypeError: m1() takes from 1 to 4 positional arguments but 5 were given
