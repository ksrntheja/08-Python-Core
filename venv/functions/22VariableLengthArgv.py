def var(*n):
    print('Printing n :', n, 'type of n :', type(n))
    if len(n) > 0:
        print('Printing n[0] :', n[0], 'type of n[0] :', type(n[0]))
    if len(n) > 1:
        print('Printing n[0] :', n[1], 'type of n[1] :', type(n[1]))


var()
print()
var(1)
print()
var(1, 2)
print()
var((1, 2), (3, 4))

# Printing n : () type of n : <class 'tuple'>
#
# Printing n : (1,) type of n : <class 'tuple'>
# Printing n[0] : 1 type of n[0] : <class 'int'>
#
# Printing n : (1, 2) type of n : <class 'tuple'>
# Printing n[0] : 1 type of n[0] : <class 'int'>
# Printing n[0] : 2 type of n[1] : <class 'int'>
#
# Printing n : ((1, 2), (3, 4)) type of n : <class 'tuple'>
# Printing n[0] : (1, 2) type of n[0] : <class 'tuple'>
# Printing n[0] : (3, 4) type of n[1] : <class 'tuple'>
