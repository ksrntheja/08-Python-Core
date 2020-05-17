class P:
    def p01(self):
        print('Parent p01 method')


class C(P):
    def c01(self):
        print('Child c01 method')


c = C()
c.p01()
c.c01()

# Parent p01 method
# Child c01 method
