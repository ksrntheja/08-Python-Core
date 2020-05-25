from zipfile import *

f = ZipFile('files.zip', 'w', ZIP_DEFLATED)
f.write('32BinaryData.py')
f.write('33BinaryDataFix.py')
f.close()
print('Done')
