x = [10, 20, 30, 40]
y = x.copy()
print(id(x))
print(id(y))
print(x is y)
y[1] = 777
print(x)
print(y)

# 140058233763976
# 140058233763912
# False
# [10, 20, 30, 40]
# [10, 777, 30, 40]
