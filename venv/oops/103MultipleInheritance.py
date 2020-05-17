class P1:
    def p01(self):
        print('Parent p01 method')


class P2:
    def p02(self):
        print('Parent p02 method')


class C(P1, P2):
    def c01(self):
        print('Child c1 method')


c = C()
c.p01()
c.p02()
c.c01()

# Parent p01 method
# Parent p02 method
# Child c1 method
