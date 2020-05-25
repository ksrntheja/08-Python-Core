f = open('abc.txt')
lines = f.readlines()
f.close()
# print(lines)
# ['Hi 1 one\n', 'Hi 2 two\n', 'Hi 3 three']
for line in lines:
    print(line, end='')

# Hi 1 one
# Hi 2 two
# Hi 3 three
