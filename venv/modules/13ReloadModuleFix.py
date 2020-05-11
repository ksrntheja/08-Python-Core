import time
from imp import reload
import TestReload

TestReload.add(10, 20)
print('Sleeping')
time.sleep(10)
print('Sleeping Done')

reload(TestReload)

TestReload.product(10, 20)

# The sum : 30
# Sleeping
# Sleeping Done
# The product : 200
