class Test:
    a = 10
    b = 20
    c = 30

    def __init__(self, name):
        self.name = name


print(Test.a)
print(Test.b)
print(Test.c)

print('Creating first Object')
t1 = Test('t1')
print(t1.a)
print(t1.b)
print(t1.c)
print(t1.name)

print('Creating second Object')
t2 = Test('t2')
print(t2.a)
print(t2.b)
print(t2.c)
print(t1.name)

print('Deleting Test.a')
del Test.a

print('Printing first Object')
# print(t1.a)
# AttributeError: 'Test' object has no attribute 'a'
print(t1.b)
print(t1.c)
print(t1.name)

print('Printing second Object')
# print(t2.a)
# AttributeError: 'Test' object has no attribute 'a'
print(t2.b)
print(t2.c)
print(t1.name)

print('Creating third Object')
t3 = Test('t3')
# print(t3.a)
# AttributeError: 'Test' object has no attribute 'a'
print(t3.b)
print(t3.c)
print(t3.name)

# 10
# 20
# 30
# Creating first Object
# 10
# 20
# 30
# t1
# Creating second Object
# 10
# 20
# 30
# t1
# Deleting Test.a
# Printing first Object
# 20
# 30
# t1
# Printing second Object
# 20
# 30
# t1
# Creating third Object
# 20
# 30
# t3
