class Test:
    a = 10

    def __init__(self):
        Test.b = 20
        del Test.a

    def m01(self):
        Test.c = 30
        del Test.b

    @classmethod
    def m02(cls):
        cls.d = 40
        del Test.c

    @staticmethod
    def m03():
        Test.e = 50
        del Test.d


print(Test.__dict__)
t = Test()
print(Test.__dict__)
t.m01()
print(Test.__dict__)
Test.m02()
print(Test.__dict__)
Test.m03()
print(Test.__dict__)
Test.f = 60
print(Test.__dict__)
del Test.e
print(Test.__dict__)

# {'__module__': '__main__', 'a': 10, '__init__': <function Test.__init__ at 0x7f62418b99d8>, 'm01': <function Test.m01 at 0x7f624183c1e0>, 'm02': <classmethod object at 0x7f62418d9be0>, 'm03': <staticmethod object at 0x7f62418d9ba8>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}
# {'__module__': '__main__', '__init__': <function Test.__init__ at 0x7f62418b99d8>, 'm01': <function Test.m01 at 0x7f624183c1e0>, 'm02': <classmethod object at 0x7f62418d9be0>, 'm03': <staticmethod object at 0x7f62418d9ba8>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'b': 20}
# {'__module__': '__main__', '__init__': <function Test.__init__ at 0x7f62418b99d8>, 'm01': <function Test.m01 at 0x7f624183c1e0>, 'm02': <classmethod object at 0x7f62418d9be0>, 'm03': <staticmethod object at 0x7f62418d9ba8>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'c': 30}
# {'__module__': '__main__', '__init__': <function Test.__init__ at 0x7f62418b99d8>, 'm01': <function Test.m01 at 0x7f624183c1e0>, 'm02': <classmethod object at 0x7f62418d9be0>, 'm03': <staticmethod object at 0x7f62418d9ba8>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'd': 40}
# {'__module__': '__main__', '__init__': <function Test.__init__ at 0x7f62418b99d8>, 'm01': <function Test.m01 at 0x7f624183c1e0>, 'm02': <classmethod object at 0x7f62418d9be0>, 'm03': <staticmethod object at 0x7f62418d9ba8>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'e': 50}
# {'__module__': '__main__', '__init__': <function Test.__init__ at 0x7f62418b99d8>, 'm01': <function Test.m01 at 0x7f624183c1e0>, 'm02': <classmethod object at 0x7f62418d9be0>, 'm03': <staticmethod object at 0x7f62418d9ba8>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'e': 50, 'f': 60}
# {'__module__': '__main__', '__init__': <function Test.__init__ at 0x7f62418b99d8>, 'm01': <function Test.m01 at 0x7f624183c1e0>, 'm02': <classmethod object at 0x7f62418d9be0>, 'm03': <staticmethod object at 0x7f62418d9ba8>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None, 'f': 60}
