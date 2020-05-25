f = open("abcccc.txt", "r+")
print("File Name: ", f.name)
print("File Mode: ", f.mode)
print("Is File Readable: ", f.readable())
print("Is File Writable: ", f.writable())
print("Is File Closed : ", f.closed)
f.close()
print("Is File Closed : ", f.closed)

# File Name:  abc.txt
# File Mode:  r+
# Is File Readable:  True
# Is File Writable:  True
# Is File Closed :  False
# Is File Closed :  True

# Traceback (most recent call last):
#   File "/Code/venv/file/06FilePropertiesr+Mode.py", line <>, in <module>
#     f = open("abcccc.txt", "r+")
# FileNotFoundError: [Errno 2] No such file or directory: 'abc.txt'
