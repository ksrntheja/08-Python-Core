def outer():
    print('outer function started')

    def inner():
        print('inner function execution')

    print('outer function returning inner function Object')
    return inner


f = outer()
print(f)
f()
f()
f()

print('f = outer vs f = outer()')
f = outer
print(f)
f()

# outer function started
# outer function returning inner function Object
# <function outer.<locals>.inner at 0x7fcad2f6ea60>
# inner function execution
# inner function execution
# inner function execution
# f = outer vs f = outer()
# <function outer at 0x7fcad4d730d0>
# outer function started
# outer function returning inner function Object