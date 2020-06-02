def test_methodA(m1C, m2C):
	print('test:test_methodA execution')

def test_methodC():
	print('test:test_methodC execution')

def test_methodB():
	print('test:test_methodB execution')

# $ python3 -m pytest -s 23PyTestAllFixturesTestScript1.py 24PyTestAllFixturesTestScript2.py 
# ============================= test session starts ==============================
# platform linux -- Python 3.6.9, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
# rootdir: /Code/venv/unittesting
# collected 6 items
#
# 23PyTestAllFixturesTestScript1.py setUpClass activity conftest
# setUp activity conftest
# test:test_methodA execution
# .tearDown activity conftest
# test:test_methodC execution
# .test:test_methodB execution
# .tearDownClass activity conftest
#
# 24PyTestAllFixturesTestScript2.py setUpClass activity conftest
# setUp activity conftest
# test1:test_methodA execution
# .tearDown activity conftest
# test1:test_methodC execution
# .test1:test_methodB execution
# .tearDownClass activity conftest
