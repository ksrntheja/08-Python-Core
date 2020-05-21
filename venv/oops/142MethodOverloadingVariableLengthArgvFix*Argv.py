class Test:
    def m1(self, *args):
        print('variable length argument method ->', args, type(args))


t = Test()
t.m1()
t.m1(10)
t.m1(10, 20)
t.m1(10, 20, 30)
t.m1(10, 20, 30, 40)

# variable length argument method -> () <class 'tuple'>
# variable length argument method -> (10,) <class 'tuple'>
# variable length argument method -> (10, 20) <class 'tuple'>
# variable length argument method -> (10, 20, 30) <class 'tuple'>
# variable length argument method -> (10, 20, 30, 40) <class 'tuple'>
