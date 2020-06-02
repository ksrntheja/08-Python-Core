import unittest


class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print('setUp method execution...')

    def est_method01(self):
        print('test method01 execution...')


    def tearDown(self):
        print('tearDown method execution...')


unittest.main()

# 
# ----------------------------------------------------------------------
# Ran 0 tests in 0.000s
#
# OK
