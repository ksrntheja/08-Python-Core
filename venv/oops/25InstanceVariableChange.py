class Test:
    def __init__(self):
        self.a = 10
        self.b = 20


t1 = Test()
t1.a = 888
t1.b = 999
t2 = Test()
print('t1:', t1.a, t1.b)
print('t2:', t2.a, t2.b)

# t1: 888 999
# t2: 10 20
