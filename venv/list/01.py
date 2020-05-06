l = []
l.append(10)
l.append('theja')
l.append(10)
print(l)

print('l[0] ->', l[0])
l[0] = 77
print('l[0] ->', l[0])
print(l)
print('l[10] ->', l[10])

# [10, 'theja', 10]
# l[0] -> 10
# l[0] -> 77
# [77, 'theja', 10]
# Traceback (most recent call last):
#   File "/Code/venv/list/01.py", line <>, in <module>
#     print('l[10] ->', l[10])
# IndexError: list index out of range
