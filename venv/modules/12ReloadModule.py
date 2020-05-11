import time
import TestReload

TestReload.add(10, 20)
print('Sleeping')
time.sleep(10)
print('Sleeping Done')

import TestReload

TestReload.product(10, 20)

# The sum : 30
# Sleeping
# Sleeping Done
# Traceback (most recent call last):
#   File "/Code/venv/modules/12ReloadModule.py", line <>, in <module>
#     TestReload.product(10, 20)
# AttributeError: module 'TestReload' has no attribute 'product'
