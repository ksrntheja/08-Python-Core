class A:
    pass


class B:
    pass


class C:
    pass


class X(A, B):
    pass


class Y(B, C):
    pass


class P(X, Y, C):
    pass


print(A.mro())
print(B.mro())
print(C.mro())
print(X.mro())
print(Y.mro())
print(P.mro())

# [<class '__main__.A'>, <class 'object'>]
# [<class '__main__.B'>, <class 'object'>]
# [<class '__main__.C'>, <class 'object'>]
# [<class '__main__.X'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
# [<class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
# [<class '__main__.P'>, <class '__main__.X'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]
