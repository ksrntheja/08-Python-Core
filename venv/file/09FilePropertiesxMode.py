f = open("abc.txt", "x")
print("File Name: ", f.name)
print("File Mode: ", f.mode)
print("Is File Readable: ", f.readable())
print("Is File Writable: ", f.writable())
print("Is File Closed : ", f.closed)
f.close()
print("Is File Closed : ", f.closed)

# Traceback (most recent call last):
#   File "/Code/venv/file/09FilePropertiesxMode.py", line <>, in <module>
#     f = open("abc.txt", "x")
# FileExistsError: [Errno 17] File exists: 'abc.txt'

# File Name:  abc.txt
# File Mode:  x
# Is File Readable:  False
# Is File Writable:  True
# Is File Closed :  False
# Is File Closed :  True
