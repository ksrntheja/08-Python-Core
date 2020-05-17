class P:
    def p01(self):
        print('Parent p01 method')


class C(P):
    def c01(self):
        print('Child c01 method')


class CC(C):
    def cc01(self):
        print('Child-Child cc01 method')


cc = CC()
cc.p01()
cc.c01()
cc.cc01()

# Parent p01 method
# Child c01 method
# Child-Child cc01 method
