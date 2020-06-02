import pytest

@pytest.yield_fixture(scope='module')
def m1C():
	print('setUpClass activity conftest')
	yield
	print('tearDownClass activity conftest')

@pytest.yield_fixture()
def m2C():
	print('setUp activity conftest')
	yield
	print('tearDown activity conftest')

