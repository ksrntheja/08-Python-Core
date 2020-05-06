n = [10, 20, 30, 40, 50, 60]
print(n)
r = reversed(n)
print(r)
print(type(r))
nr = list(r)
print(nr)
print(n)

# [10, 20, 30, 40, 50, 60]
# <list_reverseiterator object at 0x7f4fbaa25b38>
# <class 'list_reverseiterator'>
# [60, 50, 40, 30, 20, 10]
# [10, 20, 30, 40, 50, 60]
