n = int(input('Enter N:'))

for i in range(n):
    print(' ' * (n - i - 1), '* ' * (i + 1))
n = n - 1
for i in range(n):
    print(' ' * (i + 1), '* ' * (n - i))

# Enter N:5
#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
