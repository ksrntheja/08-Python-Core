f = open('abc.txt')
print(f.read(3))
print(f.readline())
print(f.readline())
print(f.read(4))
print('Remaining data')
print(f.read())
f.close()

# Hi
# 1 one
#
# Hi 2 two
#
# Hi 3
# Remaining data
#  three
