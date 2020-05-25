def decor1(func):
    def inner1():
        print('decor1 execution')

    return inner1


@decor1
def f():
    print('Original function')


f()

# decor1 execution
