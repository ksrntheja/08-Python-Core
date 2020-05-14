class Employee:
    def __init__(self):
        self.eno = 100
        self.ename = 'Theja'
        self.esal = 10000


e = Employee()
print(dir())
print(dir(e))
print(e.__dict__)

# ['Employee', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'e']
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'ename', 'eno', 'esal']
# {'eno': 100, 'ename': 'Theja', 'esal': 10000}
