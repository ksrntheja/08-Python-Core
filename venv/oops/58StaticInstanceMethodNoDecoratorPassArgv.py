class Test:

    def m01(x):
        print('m01() method')


t = Test()
t.m01(10)

# Traceback (most recent call last):
#   File "/Code/venv/oops/58StaticInstanceMethodNoDecoratorPassArgv.py", line <>, in <module>
#     t.m01(10)
# TypeError: m01() takes 1 positional argument but 2 were given
