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

	def tearDown(self):
		print('tearDown method execution...')

	@classmethod
	def tearDownClass(cls):
		print('tearDownClass method execution...')


unittest.main()

# setUpClass method execution...
# setUp method execution...
# test method01 execution...
# tearDown method execution...
# .setUp method execution...
# test method02 execution...
# tearDown method execution...
# .tearDownClass method execution...
#
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
#
# OK
#
