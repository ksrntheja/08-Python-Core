class Test:
    a = 10

    def __init__(self):
        Test.b = 20

    def m01(self):
        Test.c = 30

    @classmethod
    def m02(cls):
        cls.d1 = 40
        Test.d2 = 50

    @staticmethod
    def m03():
        Test.e = 60


print(Test.__dict__)
t = Test()
print(Test.__dict__)
t.m01()
print(Test.__dict__)
Test.m02()
print(Test.__dict__)
Test.m03()
print(Test.__dict__)
Test.f = 70
print(Test.__dict__)

# {'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x7f2379f029d8>, 'm01': <function Test.m01 at 0x7f2379e851e0>, 'm02': <classmethod object at 0x7f2379f22b70>, 'm03': <staticmethod object at 0x7f2379f2ac50>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}
# {'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x7f2379f029d8>, 'm01': <function Test.m01 at 0x7f2379e851e0>, 'm02': <classmethod object at 0x7f2379f22b70>, 'm03': <staticmethod object at 0x7f2379f2ac50>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'b': 20}
# {'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x7f2379f029d8>, 'm01': <function Test.m01 at 0x7f2379e851e0>, 'm02': <classmethod object at 0x7f2379f22b70>, 'm03': <staticmethod object at 0x7f2379f2ac50>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'b': 20, 'c': 30}
# {'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x7f2379f029d8>, 'm01': <function Test.m01 at 0x7f2379e851e0>, 'm02': <classmethod object at 0x7f2379f22b70>, 'm03': <staticmethod object at 0x7f2379f2ac50>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'b': 20, 'c': 30, 'd1': 40, 'd2': 50}
# {'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x7f2379f029d8>, 'm01': <function Test.m01 at 0x7f2379e851e0>, 'm02': <classmethod object at 0x7f2379f22b70>, 'm03': <staticmethod object at 0x7f2379f2ac50>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'b': 20, 'c': 30, 'd1': 40, 'd2': 50, 'e': 60}
# {'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x7f2379f029d8>, 'm01': <function Test.m01 at 0x7f2379e851e0>, 'm02': <classmethod object at 0x7f2379f22b70>, 'm03': <staticmethod object at 0x7f2379f2ac50>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'b': 20, 'c': 30, 'd1': 40, 'd2': 50, 'e': 60, 'f': 70}
