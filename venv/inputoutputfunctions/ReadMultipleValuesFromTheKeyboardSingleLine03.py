s = input("Enter 2 Numbers:")
l = s.split()
print('s ->', s, type(s))
print('l ->', l, type(l))
# we want a new list
# []
# [for x in l]
# [int(x) for x in l]
l1 = [int(x) for x in l]
print('l1 ->', l1, type(l1))

# Enter 2 Numbers:2 6
# s -> 2 6 <class 'str'>
# l -> ['2', '6'] <class 'list'>
# l1 -> [2, 6] <class 'list'>
