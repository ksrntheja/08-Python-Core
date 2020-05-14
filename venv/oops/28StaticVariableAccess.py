class Test:
    a = 10

    def __init__(self):
        print(self.a)
        print(Test.a)

    def m01(self):
        print(self.a)
        print(Test.a)

    @classmethod
    def m02(cls):
        print(cls.a)
        print(Test.a)

    @staticmethod
    def m03():
        print(Test.a)


t = Test()
print(Test.a)
print(t.a)
t.m01()
t.m02()
t.m03()

# 10
# 10
# 10
# 10
# 10
# 10
# 10
# 10
# 10
