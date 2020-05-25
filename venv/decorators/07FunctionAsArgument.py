def f1(func):
    func()


def f2():
    print('We cannot call f2 function directly')


f1(f2)

# We cannot call f2 function directly
