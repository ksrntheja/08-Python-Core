class Outer:
    def __init__(self):
        print("outer class object creation")

    class Inner:
        def __init__(self):
            print("inner class object creation")

        class InnerInner:
            def __init__(self):
                print("InnerInner class object creation")

            def m1(self):
                print("Nested inner class method")


outer = Outer()
inner = outer.Inner()
innerInner = inner.InnerInner()
innerInner.m1()
print()

print('Outer().Inner().InnerInner().m1()')
Outer().Inner().InnerInner().m1()

# outer class object creation
# inner class object creation
# InnerInner class object creation
# Nested inner class method
#
# Outer().Inner().InnerInner().m1()
# outer class object creation
# inner class object creation
# InnerInner class object creation
# Nested inner class method
