n = [10, 20, 30, 40, 50, 60]
print(n.pop())
print(n.pop(1))
print(n.pop(-1))
print(n)
print(n.pop(10))

# 60
# 20
# 50
# [10, 30, 40]
# Traceback (most recent call last):
#   File "/Code/venv/list/24ManipulateFunctionsIndex.py", line <>, in <module>
#     print(n.pop(10))
# IndexError: pop index out of range
