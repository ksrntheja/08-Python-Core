class Test:
    def __init__(self):
        self.__x = 10

    def __m1(self):
        print('Private method')

    def m2(self):
        print(self.__x)
        self.__m1()


print('Within class')
t = Test()
t.m2()
print('Outside class')
# print(t.__x)
# Traceback (most recent call last):
#   File "/Code/venv/oops/181Private.py", line <>, in <module>
#     print(t.__x)
# AttributeError: 'Test' object has no attribute '__x'
# t.__m1()
# Traceback (most recent call last):
#   File "Code/venv/oops/181Private.py", line <>, in <module>
#     t.__m1()
# AttributeError: 'Test' object has no attribute '__m1'

# Within class
# 10
# Private method
# Outside class
