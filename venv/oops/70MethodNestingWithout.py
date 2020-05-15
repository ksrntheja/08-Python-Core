class NestedMethods:
    def m1(self):
        a = 10
        b = 20
        print('The sum:', a + b)
        print('The product:', a * b)
        print('The difference:', a - b)
        print('The average:', (a * b) / 2)

        print()
        a = 100
        b = 200
        print('The sum:', a + b)
        print('The product:', a * b)
        print('The difference:', a - b)
        print('The average:', (a * b) / 2)


n = NestedMethods()
n.m1()

# The sum: 30
# The product: 200
# The difference: -10
# The average: 100.0
#
# The sum: 300
# The product: 20000
# The difference: -100
# The average: 10000.0
