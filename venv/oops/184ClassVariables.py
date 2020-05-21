class Test:
    x = 10
    _y = 20
    __z = 30

    def m1(self):
        print(Test.x)
        print(Test._y)
        print(Test.__z)


t = Test()
t.m1()
print(Test.x)
print(Test._y)
print(Test.__z)

# 10
# 20
# 30
# 10
# 20
# Traceback (most recent call last):
#   File "/Code/venv/oops/184ClassVariables.py", line <>, in <module>
#     print(Test.__z)
# AttributeError: type object 'Test' has no attribute '__z'
