class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def m01(self):
        del self.d

    def m02(self):
        # del self.a, self.e
        # AttributeError: e
        del self.a, self.b


t01 = Test()
print(t01.__dict__)
t01.m01()
print(t01.__dict__)
del t01.c
print(t01.__dict__)
print('t02')
t02 = Test()
del t02.a, t02.b
# t02.m02()
# AttributeError: a
print(t02.__dict__)
print('t03')
t03 = Test()
t03.m02()
print(t03.__dict__)

# {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# {'a': 10, 'b': 20, 'c': 30}
# {'a': 10, 'b': 20}
# t02
# {'c': 30, 'd': 40}
# t03
# {'c': 30, 'd': 40}
