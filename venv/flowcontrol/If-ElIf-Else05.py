a = int(input('Enter First Number:'))
b = int(input('Enter Second Number:'))
c = int(input('Enter Second Number:'))
if a < b and a < c:
    print('Smallest number is:', a)
elif b < c:
    print('Smallest number is:', b)
else:
    print('Smallest number is:', c)

# Enter First Number:10
# Enter Second Number:20
# Enter Second Number:30
# Smallest number is: 10
# Enter First Number:30
# Enter Second Number:20
# Enter Second Number:10
# Smallest number is: 10
