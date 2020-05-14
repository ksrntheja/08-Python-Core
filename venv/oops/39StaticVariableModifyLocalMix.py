class Test:
    a = 10

    def __init__(self):
        a = 200
        Test.a = 30
        print('a', a)

    def m01(self):
        # print('a', a)
        # UnboundLocalError: local variable 'a' referenced before assignment
        # Only print line
        # NameError: name 'a' is not defined
        a = 400
        Test.a = 50
        print('a', a)

    @classmethod
    def m02(cls):
        # print('a', a)
        a = 600
        Test.a = 70
        cls.a = 80
        print('a', a)

    @staticmethod
    def m03():
        # print('a', a)
        a = 700
        Test.a = 70
        print('a', a)


print(Test.a)
t = Test()
print(Test.a)
print(t.a)
t.m01()
print(Test.a)
t.m02()
print(Test.a)
t.m03()
print(Test.a)
print(t.a)

# 10
# a 200
# 30
# 30
# a 400
# 50
# a 600
# 80
# a 700
# 70
# 70
