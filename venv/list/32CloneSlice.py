x = [10, 20, 30, 40]
y = x[:]
print(id(x))
print(id(y))
print(x is y)
y[1] = 777
print(x)
print(y)

# 139828027078792
# 139828027078728
# False
# [10, 20, 30, 40]
# [10, 777, 30, 40]
