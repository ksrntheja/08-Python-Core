import pytest


def test_methodA():
    print('test_methodA execution')


def test_methodB():
    print('test_methodB execution')

# Run
# In the CWD, execute all pytest programs
# py.test
# 

# $ python3 -m pytest
# =============================================================================================== test session starts ===============================================================================================
# platform linux -- Python 3.6.9, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
# rootdir:/Code/venv/unittesting
# collected 2 items                                                                                                                                                                                                 
#
# 12PyTest01_test.py ..                                                                                                                                                                                       [100%]
#
# ================================================================================================ 2 passed in 0.01s ================================================================================================
