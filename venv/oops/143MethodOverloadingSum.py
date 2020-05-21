class Sum:
    def sum(self, *args):
        total = 0
        for x in args:
            total = total + x
        print('The sum:', total)


sum = Sum()
sum.sum()
sum.sum(10)
sum.sum(10, 20)
sum.sum(10, 20, 30)
sum.sum(10, 20, 30, 40)

# The sum: 0
# The sum: 10
# The sum: 30
# The sum: 60
# The sum: 100
