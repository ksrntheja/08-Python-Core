n = int(input('Enter N:'))

for i in range(n):
    print(' ' * (n - i - 1), '* ' * (i + 1))

# Enter N:5
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
