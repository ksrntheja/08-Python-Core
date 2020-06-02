import unittest


class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print('setUp method execution...')

    def test_method01(self):
        print('test method execution...')
        print(10 / 0)

    def tearDown(self):
        print('tearDown method execution...')


unittest.main()

# #setUp method execution...
# test method execution...
# tearDown method execution...
# E
# ======================================================================
# ERROR: test_method01 (__main__.TestCaseDemo)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "02BasicFail.py", line 10, in test_method01
#     print(10 / 0)
# ZeroDivisionError: division by zero
#
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# FAILED (errors=1)
