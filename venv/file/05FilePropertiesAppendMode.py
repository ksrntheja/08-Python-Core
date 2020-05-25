f = open("abc.txt", "a")
print("File Name: ", f.name)
print("File Mode: ", f.mode)
print("Is File Readable: ", f.readable())
print("Is File Writable: ", f.writable())
print("Is File Closed : ", f.closed)
f.close()
print("Is File Closed : ", f.closed)

# File Name:  abc.txt
# File Mode:  a
# Is File Readable:  False
# Is File Writable:  True
# Is File Closed :  False
# Is File Closed :  True
