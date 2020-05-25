fileName = input('Enter file name:')
f = open(fileName, 'w')
while True:
    data = input('Enter data:')
    f.write(data + '\n')
    option = input('Do you want to stop[yes/no]?')
    if option.lower() == 'yes':
        break
f.close()
print('Done')

# Enter file name:test
# Enter data:1
# Do you want to stop[yes/no]?no
# Enter data:2
# Do you want to stop[yes/no]?no
# Enter data:3
# Do you want to stop[yes/no]?yES
# Done

# test
# 1
# 2
# 3
