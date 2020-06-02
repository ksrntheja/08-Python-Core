import unittest

class TestCaseDemo(unittest.TestCase):
	def test_B(self):
		print('Test_B method execution...')
	def test_C(self):
		print('Test_C method execution...')
	def test_b(self):
		print('Test_b method execution...')
	def test_b(self):
		print('Test_b latest method execution...')
	def test_1(self):
		print('Test_1 method execution...')
	def test_A(self):
		print('Test_A method execution...')

unittest.main()

# Test_1 method execution...
# .Test_A method execution...
# .Test_B method execution...
# .Test_C method execution...
# .Test_b latest method execution...
# .
# ----------------------------------------------------------------------
# Ran 5 tests in 0.000s
#
# OK
