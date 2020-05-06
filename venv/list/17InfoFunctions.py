n = []
print(n)
print('len(n) -> ', len(n))
n = [10, 20, 30, 40]
print(n)
print('len(n) -> ', len(n))

print()

n = [1, 2, 2, 2, 2, 3, 3]
print(n.count(1))
print(n.count(2))
print(n.count(3))
print(n.count(4))

print()

print(n.index(1))
print(n.index(2))
print(n.index(3))
print(n.index(4))

# []
# len(n) ->  0
# [10, 20, 30, 40]
# len(n) ->  4
#
# 1
# 4
# 2
# 0
#
# 0
# 1
# 5
# Traceback (most recent call last):
#   File "/Code/venv/list/17InfoFunctions.py", line <>, in <module>
#     print(n.index(4))
# ValueError: 4 is not in list
