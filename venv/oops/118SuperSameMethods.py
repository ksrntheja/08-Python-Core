class P:
    def m1(self):
        print('Parent Method')


class C(P):
    def m1(self):
        self.m1()
        print('Child Method')


c = C()
c.m1()

# Traceback (most recent call last):
#   File "/Code/venv/oops/118SuperSameMethods.py", line 13, in <module>
#     c.m1()
#   File "/Code/venv/oops/118SuperSameMethods.py", line 8, in m1
#     self.m1()
#   File "/Code/venv/oops/118SuperSameMethods.py", line 8, in m1
#     self.m1()
#   File "/Code/venv/oops/118SuperSameMethods.py", line 8, in m1
#     self.m1()
#   [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded
