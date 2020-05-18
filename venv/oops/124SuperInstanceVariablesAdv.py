class P:
    a = 10

    def __init__(self):
        print('P constructor')
        self.b = 20


class C(P):

    def __init__(self):
        self.b = 30

    def method(self):
        print('Using self to access parent members')
        print(self.a)
        print(self.b)
        print('Using super() to access parent members')
        print(super().a)


c = C()
c.method()

# Using self to access parent members
# 10
# 30
# Using super() to access parent members
# 10
