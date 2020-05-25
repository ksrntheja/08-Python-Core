f = open("abc.txt", "r")
print('tell', f.tell())
f.seek(3)
print('tell', f.tell())
print(f.read(2))
f.seek(10)
print('tell', f.tell())
print(f.read())
f.seek(0)
print('tell', f.tell())
print(f.read())
f.seek(100)
print('tell', f.tell())
print(f.read())

`# abc.txt
# Hi One
# Hi Ten
# Hi Bye`

# tell 0
# tell 3
# On
# tell 10
# Ten
# Hi Bye
# tell 0
# Hi One
# Hi Ten
# Hi Bye
# tell 100
#
#
