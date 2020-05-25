f = open("abc.txt", "r")
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.read(1))
print(f.tell())

print(f.read(3))
print(f.tell())
print(f.read(1))
print('Done')
f.close()

# abc.txt
# Hi One
# Hi Ten
# Hi Bye

# 0
# Hi
# 2
#
# 3
# One
# 6
#
#
# Done
