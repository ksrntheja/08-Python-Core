f = open('abc.txt')
line = f.readline()
while line != '':
    print(line, end='')
    line = f.readline()
f.close()

# Hi 1 one
# Hi 2 two
# Hi 3 three
