a = 10
b = 10
print(a is b)
x = True
y = True
print(x is y)

print()

a = "theja"
b = "theja"
print(id(a))
print(id(b))
print(a is b)

print()

list1 = ["one", "two", "three"]
list2 = ["one", "two", "three"]
print(id(list1))
print(id(list2))
print(list1 is list2)
print(list1 is not list2)
print(list1 == list2)

# True
# True
#
# 140174737417080
# 140174737417080
# True
#
# 140174705641672
# 140174705641608
# False
# True
# True
