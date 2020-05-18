class D:
    pass


class E:
    pass


class F:
    pass


class B(D, E):
    pass


class C(D, F):
    pass


class A(B, C):
    pass


print(D.mro())
print(E.mro())
print(F.mro())
print(B.mro())
print(C.mro())
print(A.mro())

# [<class '__main__.D'>, <class 'object'>]
# [<class '__main__.E'>, <class 'object'>]
# [<class '__main__.F'>, <class 'object'>]
# [<class '__main__.B'>, <class '__main__.D'>, <class '__main__.E'>, <class 'object'>]
# [<class '__main__.C'>, <class '__main__.D'>, <class '__main__.F'>, <class 'object'>]
# [<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>]
