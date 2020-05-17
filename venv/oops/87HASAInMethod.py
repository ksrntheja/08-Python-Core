class X:
    a = 10

    def __init__(self):
        self.b = 20

    def m01(self):
        print("m01 method of X class")


class Y:
    c = 30

    def __init__(self):
        self.d = 40

    def m02(self):
        print("m02 method of Y class")

    def m03(self):
        x = X()
        print(X.a)
        print(x.b)
        x.m01()
        print(Y.c)
        print(self.d)
        self.m02()
        print("m03 method of Y class")


y = Y()
y.m03()

# 10
# 20
# m01 method of X class
# 30
# 40
# m02 method of Y class
# m03 method of Y class
