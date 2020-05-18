class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(C, B):
    pass


print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())

# [<class '__main__.A'>, <class 'object'>]
# [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
# [<class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
