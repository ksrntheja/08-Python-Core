a = 100


class Test:
    a = 10

    def __init__(self):
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


print(a)
print(Test.a)
t = Test()
print(a)
print(Test.a)
t.m01()
print(a)
print(Test.a)
t.m02()
print(a)
print(Test.a)
t.m03()
print(a)
print(Test.a)

# 100
# 10
# 100
# 10
# 30
# 10
# 40
# 10
# 50
# 10
