def decor1(func):
    def inner1():
        print('decor1 execution')

    return inner1


def decor2(func):
    def inner2():
        print('decor2 execution')

    return inner2


@decor1
@decor2
def f():
    print('Original function')


f()

# decor1 execution
