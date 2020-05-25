f = open('abcd.txt', 'a')
f.write('Hi1\n')
f.write('Hi2\n')
f.write('Hi3')
f.write('Hi4\n')
print('Write done')
f.close()

# Write done

# abcd.txt
# Hi1
# Hi2Hi3
# Hi1
# Hi2
# Hi3Hi4
