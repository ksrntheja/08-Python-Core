import os
from datetime import *

stats = os.stat('42StatPrintSome.py')
print('type(stats):', type(stats))

print("File Size in Bytes:", stats.st_size)
print("File Last Accessed Time:", datetime.fromtimestamp(stats.st_atime))
print("File Last Modified Time:", datetime.fromtimestamp(stats.st_mtime))

# type(stats): <class 'os.stat_result'>
# File Size in Bytes: 300
# File Last Accessed Time: 2020-05-25 10:14:45.187551
# File Last Modified Time: 2020-05-25 10:14:42.195672
