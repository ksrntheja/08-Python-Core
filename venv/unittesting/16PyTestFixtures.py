import pytest

@pytest.fixture
def m1():
	print('setUp method')

def test_methodA():
	print('test_methodA execution')

def test_methodB():
	print('test_methodB execution')


# $ python3 -m pytest -s 16PyTestFixtures.py
# ========================= test session starts ==========================
# platform linux -- Python 3.6.9, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
# rootdir: /Code/venv/unittesting
# collected 2 items                                                      
# 
# 16PyTestFixtures.py test_methodA execution
# .test_methodB execution
# .
# 
# ========================== 2 passed in 0.01s ===========================

# $ python3 -m pytest -s -v 16PyTestFixtures.py::test_methodB
# =============================================================================================== test session starts ===============================================================================================
# platform linux -- Python 3.6.9, pytest-5.4.2, py-1.8.1, pluggy-0.13.1 -- /usr/bin/python3
# cachedir: .pytest_cache
# rootdir: /Code/venv/unittesting
# collected 1 item
#
# 16PyTestFixtures.py::test_methodB test_methodB execution
# PASSED
#
# ================================================================================================ 1 passed in 0.01s ================================================================================================
