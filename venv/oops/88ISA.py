class P:
    def m1(self):
        print("Parent class method")


class C(P):
    def m2(self):
        print("Child class method")


c = C()
c.m1()
c.m2()

# Parent class method
# Child class method
