n = [1, 2, 2, 2, 2, 3, 3]
x = int(input('Enter element to remove:'))
if x in n:
    n.remove(x)
    print(n)
else:
    print(x, 'not available in list')

# Enter element to remove:2
# [1, 2, 2, 2, 3, 3]

# Enter element to remove:4
# 4 not available in list
