read = open('input.txt')
write = open('output.txt', 'w')

data = read.read()
write.write(data)

read.close()
write.close()

print('Done')

# Done