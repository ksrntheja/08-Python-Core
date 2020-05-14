class Test:
    print('Within the class directly but from out side of any method')
    a = 10

    def __init__(self):
        print('Constructor start...')
        print('Inside constructor by using class name')
        Test.a = 20
        print('self.a    ->', self.a)
        print('Test.a    ->', Test.a)
        print('Constructor end...')

    def m01(self):
        print('m01(self) start...')
        print('self.a    ->', self.a)
        print('Test.a    ->', Test.a)
        print('Inside instance method by using class name')
        Test.a = 30
        print('self.a    ->', self.a)
        print('Test.a    ->', Test.a)
        print('m01(self) end...')

    @classmethod
    def m02(cls):
        print('m02(cls) start...')
        print('cls.a    ->', cls.a)
        print('Test.a   ->', Test.a)
        print('Inside classmethod by using cls variable')
        cls.a = 40
        print('cls.a    ->', cls.a)
        print('Test.a   ->', Test.a)
        print('Inside classmethod by using class name')
        Test.a = 50
        print('cls.a   ->', cls.a)
        print('Test.a  ->', Test.a)
        print('m02(cls) end...')

    @staticmethod
    def m03():
        print('m03() start...')
        print('Test.a  ->', Test.a)
        print('Inside static method by using class name')
        Test.a = 60
        print('Test.a  ->', Test.a)
        print('m03(cls) end...')


print('Outside class start...')
print("Test.a   ->", Test.a)
print('Creating Test Object')
t = Test()
print("Test.a   ->", Test.a)
print("t.a      ->", t.a)
t.m01()
Test.m02()
Test.m03()
print("Test.a   ->", Test.a)
print("t.a      ->", t.a)
print('From Outside of class by using class name')
Test.a = 70
print("Test.a   ->", Test.a)
print("t.a      ->", t.a)
print('Outside class end...')

# Within the class directly but from out side of any method
# Outside class start...
# Test.a   -> 10
# Creating Test Object
# Constructor start...
# Inside constructor by using class name
# self.a    -> 20
# Test.a    -> 20
# Constructor end...
# Test.a   -> 20
# t.a      -> 20
# m01(self) start...
# self.a    -> 20
# Test.a    -> 20
# Inside instance method by using class name
# self.a    -> 30
# Test.a    -> 30
# m01(self) end...
# m02(cls) start...
# cls.a    -> 30
# Test.a   -> 30
# Inside classmethod by using cls variable
# cls.a    -> 40
# Test.a   -> 40
# Inside classmethod by using class name
# cls.a   -> 50
# Test.a  -> 50
# m02(cls) end...
# m03() start...
# Test.a  -> 50
# Inside static method by using class name
# Test.a  -> 60
# m03(cls) end...
# Test.a   -> 60
# t.a      -> 60
# From Outside of class by using class name
# Test.a   -> 70
# t.a      -> 70
# Outside class end...
