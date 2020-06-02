import unittest


class TestCaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass method execution...')

    def setUp(self):
        print('setUp method execution...')

    def test_method01(self):
        print('test method01 execution...')

    def test_method02(self):
        print('test method02 execution...')
        print(10 / 0)

    def test_method03(self):
        print('test method03 execution...')

    def test_method04(self):
        print('test method04 execution...')
        print(10 / 0)

    def tearDown(self):
        print('tearDown method execution...')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass method execution...')


unittest.main()

#  
# setUpClass method execution...
# setUp method execution...
# test method01 execution...
# tearDown method execution...
# .setUp method execution...
# test method02 execution...
# tearDown method execution...
# EsetUp method execution...
# test method03 execution...
# tearDown method execution...
# .setUp method execution...
# test method04 execution...
# tearDown method execution...
# EtearDownClass method execution...
#
# ======================================================================
# ERROR: test_method02 (__main__.TestCaseDemo)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "07SetUpClassMethodFail.py", line 17, in test_method02
#     print(10/0)
# ZeroDivisionError: division by zero
#
# ======================================================================
# ERROR: test_method04 (__main__.TestCaseDemo)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "07SetUpClassMethodFail.py", line 24, in test_method04
#     print(10/0)
# ZeroDivisionError: division by zero
#
# ----------------------------------------------------------------------
# Ran 4 tests in 0.001s
#
# FAILED (errors=2)
