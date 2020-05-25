def wish(name):
    print('Hi', name)


greeting = wish

print(wish)
print(id(wish))

print(wish)
print(id(wish))

wish('Theja')
greeting('Ksrn')

print('Deleting wish')
del wish

# wish('Theja')
# Traceback (most recent call last):
#   File "//Code/venv/decorators/02FunctionAliasing.py", line <>, in <module
#     wish('Theja')
# NameError: name 'wish' is not defined
greeting('Ksrn')

# <function wish at 0x7f2ce94bc0d0>
# 139830869344464
# <function wish at 0x7f2ce94bc0d0>
# 139830869344464
# Hi Theja
# Hi Ksrn
# Deleting wish
# Hi Ksrn
