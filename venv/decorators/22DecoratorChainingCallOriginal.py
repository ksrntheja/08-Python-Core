def decor1(func):
    def inner1():
        print('decor1 execution')
        func()

    return inner1


@decor1
def f():
    print('Original function')


f()

# decor1 execution
# Original function
