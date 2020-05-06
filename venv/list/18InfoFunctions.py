n = [1, 2, 2, 2, 2, 3, 3]
x = int(input('Enter element to find:'))
if x in n:
    print('{} present at index {}'.format(x, n.index(x)))
else:
    print(x, 'not available in list')

# Enter element to find:2
# 2 present at index 1

# Enter element to find:4
# 4 not available in list
