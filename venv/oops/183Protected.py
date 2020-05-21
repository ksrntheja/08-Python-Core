class Test:
    def __init__(self):
        self._x = 10

    def _m1(self):
        print('Protected method')


class SubTest(Test):
    def m2(self):
        print(self._x)


print('Within class')
t = Test()
t._m1()
print(t._x)
print('Outside class within child-class')
st = SubTest()
st._m1()
st.m2()
print(st._x)

# Within class
# Protected method
# 10
# Outside class within child-class
# Protected method
# 10
# 10
