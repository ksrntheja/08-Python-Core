class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m(self):
        self.c = 30


t = Test()  # a,b will be added to Object
t.m()  # c will be added to Object
print(dir())
print(dir(t))
print(t.__dict__)
print('Adding outside...')
t.d = 40  # c will be added to Object
print(dir())
print(dir(t))
print(t.__dict__)

# ['Test', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 't']
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'b', 'c', 'm']
# {'a': 10, 'b': 20, 'c': 30}
# Adding outside...
# ['Test', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 't']
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'b', 'c', 'd', 'm']
# {'a': 10, 'b': 20, 'c': 30, 'd': 40}
