class P1:
    def p(self):
        print('Parent P1 method')


class P2:
    def p(self):
        print('Parent P2 method')


class C(P1, P2):
    def c01(self):
        print('Child c1 method')


c = C()
c.p()
c.c01()

# Parent P1 method
# Child c1 method
