a = [10, 20, 30]
# b = (40, 50, 60)
# TypeError: can only concatenate list (not "tuple") to list
b = [40, 50, 60]
c = a + b
print(c)

c = c + [70]
print(c)

c = c + 80
print(c)

# [10, 20, 30, 40, 50, 60]
# [10, 20, 30, 40, 50, 60, 70]
# Traceback (most recent call last):
#   File "/Code/venv/list/10+.py", line <>, in <module>
#     c = c + 80
# TypeError: can only concatenate list (not "int") to list
