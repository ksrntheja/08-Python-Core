import sys


class Test:
    pass


t1 = Test()
print(sys.getrefcount(t1))
t2 = t1
print(sys.getrefcount(t1))
t3 = t1
print(sys.getrefcount(t1))
t4 = t1
print(sys.getrefcount(t1))
del t3, t4
print(sys.getrefcount(t1))

# 2
# 3
# 4
# 5
# 3
