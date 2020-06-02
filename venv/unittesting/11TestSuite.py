import unittest
from testcase1 import *
from testcase2 import *

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)

ts = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner().run(ts)

# TestCase1:setUp
# TestCase1:test1
# TestCase1:tearDown
# .TestCase1:setUp
# TestCase1:test2
# TestCase1:tearDown
# .TestCase2:setUp
# TestCase2:test1
# TestCase2:tearDown
# .
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s
#
# OK
#
