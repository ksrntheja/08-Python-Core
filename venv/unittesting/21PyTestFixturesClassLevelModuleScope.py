import pytest


@pytest.yield_fixture(scope='module')
def m1():
    print('setUpClass activity')
    yield
    print('tearDownClass activity')


def test_methodA(m1):
    print('test_methodA execution')


def test_methodC():
    print('test_methodC execution')


def test_methodB():
    print('test_methodB execution')

# $ python3 -m pytest -s 21PyTestFixturesClassLevelModuleScope.py 
# ========================== test session starts ==========================
# platform linux -- Python 3.6.9, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
# rootdir: /Code/venv/unittesting
# collected 3 items
#
# 21PyTestFixturesClassLevelModuleScope.py setUpClass activity
# test_methodA execution
# .test_methodC execution
# .test_methodB execution
# .tearDownClass activity
#
#
# =========================== 3 passed in 0.01s ===========================
