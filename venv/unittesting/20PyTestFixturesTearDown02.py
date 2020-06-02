import pytest

@pytest.yield_fixture()
def m1():
	yield
	print('tearDown activity')

def test_methodA(m1):
	print('test_methodA execution')

def test_methodC():
	print('test_methodC execution')

def test_methodB():
	print('test_methodB execution')

# $ python3 -m pytest -s 20PyTestFixturesTearDown02.py 
# ========================== test session starts ==========================
# platform linux -- Python 3.6.9, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
# rootdir: /Code/venv/unittesting
# collected 3 items
#
# 20PyTestFixturesTearDown02.py test_methodA execution
# .tearDown activity
# test_methodC execution
# .test_methodB execution
# .
#
# =========================== 3 passed in 0.01s ===========================
