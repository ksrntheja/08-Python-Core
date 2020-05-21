class Test:
    def m1(self, x):
        print('{}-arg method'.format(x.__class__.__name__))


t = Test()
t.m1(10)
t.m1(10.5)
t.m1('theja')

# int-arg method
# float-arg method
# str-arg method
