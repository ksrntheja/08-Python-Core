class Outer:
    def __init__(self):
        print("outer class object creation")

    class Inner:
        def __init__(self):
            print("inner class object creation")

        class InnerInner:
            def __init__(self):
                print("InnerInner class object creation")

            @staticmethod
            def m1():
                print("Nested inner class static method")


print('Outer().Inner().InnerInner().m1()')
Outer().Inner().InnerInner().m1()
print()

print('Outer().Inner().InnerInner.m1()')
Outer().Inner().InnerInner.m1()

# Outer().Inner().InnerInner().m1()
# outer class object creation
# inner class object creation
# InnerInner class object creation
# Nested inner class static method
#
# Outer().Inner().InnerInner.m1()
# outer class object creation
# inner class object creation
# Nested inner class static method
