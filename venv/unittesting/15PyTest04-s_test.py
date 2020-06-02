import pytest


def test_methodA():
    print('test_methodA execution')


def test_methodB():
    print('test_methodB execution')

# python3 -m pytest 15PyTest04-s_test.py
# ============================= test session starts ==============================
# platform linux -- Python 3.6.9, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
# rootdir:/Code/venv/unittesting
# collected 2 items
#
# 15PyTest04-s_test.py ..                                                  [100%]
#
# ============================== 2 passed in 0.01s ===============================
# ksrntheja@ksrntheja-Lenovo-IdeaPad-L340-15IWL:/Code/venv/unittesting$ python3 -m pytest -s 15PyTest04-s_test.py
# ============================= test session starts ==============================
# platform linux -- Python 3.6.9, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
# rootdir:/Code/venv/unittesting
# collected 2 items
#
# 15PyTest04-s_test.py test_methodA execution
# .test_methodB execution
# .
#
# ksrntheja@ksrntheja-Lenovo-IdeaPad-L340-15IWL:~/Code/venv/unittesting$ python3 -m pytest -s -v 15PyTest04-s_test.py
# =============================================================================================== test session starts ===============================================================================================
# platform linux -- Python 3.6.9, pytest-5.4.2, py-1.8.1, pluggy-0.13.1 -- /usr/bin/python3
# cachedir: .pytest_cache
# rootdir:/Code/venv/unittesting
# collected 2 items
#
# 15PyTest04-s_test.py::test_methodA test_methodA execution
# PASSED
# 15PyTest04-s_test.py::test_methodB test_methodB execution
# PASSED
#
# ================================================================================================ 2 passed in 0.01s ================================================================================================
