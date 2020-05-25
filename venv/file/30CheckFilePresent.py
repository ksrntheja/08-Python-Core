import os, sys

fname = input("Enter File Name: ")
if os.path.isfile(fname):
    print("File exists:", fname)
    f = open(fname, "r")
else:
    print("File does not exist:", fname)
    sys.exit(0)

print("The content of file is:")
data = f.read()
print(data)
f.close()

# Enter File Name: abc.txt
# File exists: abc.txt
# The content of file is:
# All Students are GEMSIDS

# Enter File Name: hi
# File does not exist: hi
