a = 10


def f01():
    global a
    a = 20
    print(a)


def f02():
    print(a)


f01()
f02()

# 20
# 20
