def f01():
    a = 10
    print(a, id(a))


def f02():
    a = 10
    print(a, id(a))


f01()
f02()

# 10 10914784
# 10 10914784
