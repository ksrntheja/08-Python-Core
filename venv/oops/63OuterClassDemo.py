class Outer:
    def __init__(self):
        print("outer class object creation")

    class Inner:
        def __init__(self):
            print("inner class object creation")

        def m1(self):
            print("inner class method")


outer01 = Outer()
# i = Inner()
# NameError: name 'Inner' is not defined
inner01 = outer01.Inner()
inner01.m1()
print()

print('Outer().Inner()')
inner02 = Outer().Inner()
inner02.m1()
print()

print('Outer().Inner().m1()')
Outer().Inner().m1()
print()

# outer class object creation
# inner class object creation
# inner class method
#
# Outer().Inner()
# outer class object creation
# inner class object creation
# inner class method
#
# Outer().Inner().m1()
# outer class object creation
# inner class object creation
# inner class method
