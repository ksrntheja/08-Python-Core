def outer():
    print('outer function started')

    def inner():
        print('inner function execution')

    print('outer function returning inner function')
    return inner


f = outer()
print(f)
f()
f()
f()

# outer function started
# outer function returning inner function
# <function outer.<locals>.inner at 0x7efffdd68a60>
# inner function execution
# inner function execution
# inner function execution
