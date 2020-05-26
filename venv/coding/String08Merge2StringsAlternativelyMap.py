s1 = input('Enter first  String:')
s2 = input('Enter second String:')

l = list(map(lambda x, y: x + y, s1, s2))
print(''.join(l))

print('Using function instead of lambda:')


def function(x, y):
    print('x:', x)
    print('y:', y)
    return x + y


l = list(map(function, s1, s2))
print(''.join(l))

# Enter first  String:One
# Enter second String:Two
# OTnweo
# Using function instead of lambda:
# x: O
# y: T
# x: n
# y: w
# x: e
# y: o
# OTnweo
