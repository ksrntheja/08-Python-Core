f = open('Hmm.png')
data = f.read()
f.close()
print('type(data)', type(data))
f = open('myhmm.png')
f.write(data)
f.close()
print('Done')

# Traceback (most recent call last):
#   File "/Code/venv/file/32BinaryData.py", line <>, in <module>
#     data = f.read()
#   File "/usr/lib/python3.6/codecs.py", line 321, in decode
#     (result, consumed) = self._buffer_decode(data, self.errors, final)
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte
