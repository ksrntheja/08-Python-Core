class Test:
    a = 10

    def __init__(self):
        global a
        # Global variable 'a' is undefined at the module level
        a = 20

    def m01(self):
        global a
        a = 30

    @classmethod
    def m02(cls):
        global a
        a = 40

    @staticmethod
    def m03():
        global a
        a = 50


print(Test.a)
t = Test()
print(Test.a)
t.m01()
print(Test.a)
t.m02()
print(Test.a)
t.m03()
print(Test.a)

# 10
# 10
# 10
# 10
# 10
