x = [10, 20, 30, 40]
y = x
print(id(x))
print(id(y))
y[1] = 777
print(x)
print(y)

# 139895975245960
# 139895975245960
# [10, 777, 30, 40]
# [10, 777, 30, 40]
