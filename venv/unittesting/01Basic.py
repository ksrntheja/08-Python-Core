import unittest


class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print('setUp method execution...')

    def test_method01(self):
        print('test method execution...')

    def tearDown(self):
        print('tearDown method execution...')


unittest.main()

# python3 01Basic.py
# setUp method execution...
# test method execution...
# tearDown method execution...
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
