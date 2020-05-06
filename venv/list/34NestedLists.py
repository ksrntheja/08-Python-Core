l = [10, 20, [30, 40]]
print(l)
print(type(l))
print('l[0] ->', l[0], type(l[0]))
print('l[1] ->', l[1], type(l[1]))
print('l[2] ->', l[2], type(l[2]))
# print(type(l[3]))
# Traceback (most recent call last):
#   File "/Code/venv/list/05NestedLists.py", line <>, in <module>
#     print(type(l[3]))
# IndexError: list index out of range
print('l[2][0] ->', l[2][0], type(l[2][0]))
print('l[2][1] ->', l[2][1], type(l[2][1]))

# [10, 20, [30, 40]]
# <class 'list'>
# l[0] -> 10 <class 'int'>
# l[1] -> 20 <class 'int'>
# l[2] -> [30, 40] <class 'list'>
# l[2][0] -> 30 <class 'int'>
# l[2][1] -> 40 <class 'int'>
