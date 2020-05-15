class Math:

    @staticmethod
    def add(x, y):
        print('The Sum:', x + y)

    @staticmethod
    def product(x, y):
        print('The Product:', x * y)

    @staticmethod
    def average(x, y):
        print('The average:', (x + y) / 2)

    @staticmethod
    def cls(cls):
        print('Hi', cls)

    @staticmethod
    def self(self):
        print('Hi', self)


Math.add(10, 20)
Math.product(10, 20)
Math.average(10, 20)
Math.cls('Theja')

# The Sum: 30
# The Product: 200
# The average: 15.0
