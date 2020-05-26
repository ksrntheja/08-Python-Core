n = int(input('Enter N:'))

for i in range(n):
    for j in range(i + 1):
        print('*', end=' ')
    print()

# Enter N:5
# *
# * *
# * * *
# * * * *
# * * * * *
