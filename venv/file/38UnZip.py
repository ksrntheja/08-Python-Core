from zipfile import *

# f = ZipFile('files.zip', 'r', ZIP_STORED)
f = ZipFile('files.zip', 'r')
names = f.namelist()
print('Files ->', names)
for name in names:
    print("File Name: ", name)
    print("The Content of this file is:")
    f1 = open(name, 'r')
    print(f1.read())
    f1.close()
    print()
f.close()
print('Done')

# Files -> ['32BinaryData.py', '33BinaryDataFix.py']
# File Name:  32BinaryData.py
# The Content of this file is:
# f = open('Hmm.png')
# data = f.read()
# f.close()
# print('type(data)', type(data))
# f = open('myhmm.png')
# f.write(data)
# f.close()
# print('Done')
#
# # Traceback (most recent call last):
# #   File "/Code/venv/file/32BinaryData.py", line <>, in <module>
# #     data = f.read()
# #   File "/usr/lib/python3.6/codecs.py", line 321, in decode
# #     (result, consumed) = self._buffer_decode(data, self.errors, final)
# # UnicodeDecodeError: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte
#
#
# File Name:  33BinaryDataFix.py
# The Content of this file is:
# f = open('Hmm.png', 'rb')
# data = f.read()
# f.close()
# print('type(data)', type(data))
# f = open('myhmm.png', 'wb')
# f.write(data)
# f.close()
# print('Done')
#
# # type(data) <class 'bytes'>
# # Done
#
#
# Done
