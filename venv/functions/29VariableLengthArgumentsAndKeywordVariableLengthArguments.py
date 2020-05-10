def var(*args, **kwargs):
    print('Printing args   :', args, 'type of args :', type(args))
    print('Printing kwargs :', kwargs, 'type of kwargs :', type(kwargs))


var()
print()
var(10, 20, name='Theja', rollNo=101)
print()

# Printing args   : () type of args : <class 'tuple'>
# Printing kwargs : {} type of kwargs : <class 'dict'>
#
# Printing args   : (10, 20) type of args : <class 'tuple'>
# Printing kwargs : {'name': 'Theja', 'rollNo': 101} type of kwargs : <class 'dict'>
