def test_methodC():
    print('test_methodC execution')


def test_methodA():
    print('test_methodA execution')


def test_methodB():
    print('test_methodB execution')

# $ python3 -m pytest -s -v 25PyTestOrder.py
# ============================= test session starts ==============================
# platform linux -- Python 3.6.9, pytest-5.4.2, py-1.8.1, pluggy-0.13.1 -- /usr/bin/python3
# cachedir: .pytest_cache
# metadata: {'Python': '3.6.9', 'Platform': 'Linux-5.3.0-53-generic-x86_64-with-Ubuntu-18.04-bionic', 'Packages': {'pytest': '5.4.2', 'py': '1.8.1', 'pluggy': '0.13.1'}, 'Plugins': {'html': '2.1.1', 'ordering': '0.6', 'metadata': '1.9.0'}, 'JAVA_HOME': '/usr/java/jdk-11.0.4'}
# rootdir: /Code/venv/unittesting
# plugins: html-2.1.1, ordering-0.6, metadata-1.9.0
# collected 3 items
#
# 25PyTestOrder.py::test_methodC test_methodC execution
# PASSED
# 25PyTestOrder.py::test_methodA test_methodA execution
# PASSED
# 25PyTestOrder.py::test_methodB test_methodB execution
# PASSED
