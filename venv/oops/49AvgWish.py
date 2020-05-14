class Test:

    @staticmethod
    def average(list1):
        result = sum(list1) / len(list1)
        print('The Avg:', result)

    @staticmethod
    def wish(name):
        for i in range(10):
            print('Good Evening', i, name)


list1 = [10, 20, 30, 40]
Test.average(list1)

Test.wish('Theja')

# The Avg: 25.0
# Good Evening 0 Theja
# Good Evening 1 Theja
# Good Evening 2 Theja
# Good Evening 3 Theja
# Good Evening 4 Theja
# Good Evening 5 Theja
# Good Evening 6 Theja
# Good Evening 7 Theja
# Good Evening 8 Theja
# Good Evening 9 Theja
