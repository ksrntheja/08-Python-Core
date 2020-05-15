class NestedMethods:
    def m1(self):
        def calc(a, b):
            print('The sum:', a + b)
            print('The product:', a * b)
            print('The difference:', a - b)
            print('The average:', (a * b) / 2)
            print()

        calc(10, 20)
        calc(100, 200)


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
