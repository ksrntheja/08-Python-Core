import unittest


class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print('setUp method execution...')

    def test_method01(self):
        print('test method01 execution...')


    def tearDown(self):
        print('tearDown method execution...')


unittest.main()

# setUp method execution...
# test method01 execution...
# tearDown method execution...
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
