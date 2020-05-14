class Test:
    a = 10

    def m1(self):
        self.a = 888


t = Test()
t.m1()
print(Test.a)
print(t.a)

# 10
# 888
