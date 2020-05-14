class Test:
    def m1(self):
        a = 1000
        print(a)

    def m2(self):
        b = 2000
        print(a)
        print(b)


t = Test()
t.m1()
t.m2()

# 1000
# Traceback (most recent call last):
#   File "/Code/venv/oops/48LocalVariablesError.py", line <>, in <module>
#     t.m2()
#   File "/Code/venv/oops/48LocalVariablesError.py", line <>, in m2
#     print(a)
# NameError: name 'a' is not defined
