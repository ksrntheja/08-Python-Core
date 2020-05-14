class Test:
    a = 10
    b = 20
    c = 30

    @classmethod
    def m1(cls):
        del cls.a
        del Test.b


print(Test.__dict__)
del Test.c
Test.m1()
print(Test.__dict__)

# {'__module__': '__main__', 'a': 10, 'b': 20, 'c': 30, 'm1': <classmethod object at 0x7f50c8e0ab70>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}
# {'__module__': '__main__', 'm1': <classmethod object at 0x7f50c8e0ab70>, '__dict__': <attribute '__dict__' of 'Test' objects>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}
