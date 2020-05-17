class P:
    def p01(self):
        print('Parent p01 method')


class C1(P):
    def c1m01(self):
        print('Child c1m01 method')


class C2(P):
    def c2m01(self):
        print('Child c2m01 method')


print('C1')
c1 = C1()
c1.p01()
c1.c1m01()
# c1.c2m01()
# Traceback (most recent call last):
#   File "/Code/venv/oops/102HierarchicalInheritance.py", line <>, in <module>
#     c1.c2m01()
# AttributeError: 'C1' object has no attribute 'c2m01'

print('C2')
c2 = C2()
c2.p01()
# c2.c1m01()
# Traceback (most recent call last):
#   File "/Code/venv/oops/102HierarchicalInheritance.py", line <>, in <module>
#     c2.c1m01()
# AttributeError: 'C2' object has no attribute 'c1m01'
c2.c2m01()

# C1
# Parent p01 method
# Child c1m01 method
# C2
# Parent p01 method
# Child c2m01 method
