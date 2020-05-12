from setuptools import setup, find_packages

setup(name='appinstalldemo',
      version='0.1',
      packages=find_packages()
      )

# Uninstall a package:
# $ pip3 uninstall appinstalldemoUninstalling appinstalldemo-0.1:
#   /home/ksrntheja/.local/lib/python3.6/site-packages/appinstalldemo-0.1.egg-info
#   /home/ksrntheja/.local/lib/python3.6/site-packages/appinstalldemo/__init__.py
#   /home/ksrntheja/.local/lib/python3.6/site-packages/appinstalldemo/__pycache__/__init__.cpython-36.pyc
#   /home/ksrntheja/.local/lib/python3.6/site-packages/appinstalldemo/__pycache__/appdemo.cpython-36.pyc
#   /home/ksrntheja/.local/lib/python3.6/site-packages/appinstalldemo/appdemo.py
# Proceed (y/n)? y
#   Successfully uninstalled appinstalldemo-0.1

# /packageinstallapp$ pip3 install .
# Processing /Code/venv/packages/packageinstallapp
# Installing collected packages: appinstalldemo
#   Running setup.py install for appinstalldemo ... done
# Successfully installed appinstalldemo-0.1
