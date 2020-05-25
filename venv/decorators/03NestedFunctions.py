def outer():
    print('outer function started')

    def inner():
        print('inner function execution')

    print('outer function completed')


outer()

# outer function started
# outer function completed
