class P:
    def m1(self):
        print('Parent Method')


class C(P):
    def m2(self):
        self.m1()
        print('Child Method')


c = C()
c.m2()

# Parent Method
# Child Method
