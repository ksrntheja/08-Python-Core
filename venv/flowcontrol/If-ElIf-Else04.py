a = int(input('Enter First Number:'))
b = int(input('Enter Second Number:'))
c = int(input('Enter Second Number:'))
if a > b & a > c:
    print('Biggest number is:', a)
elif b > c:
    print('Biggest number is:', b)
else:
    print('Biggest number is:', c)

# Enter First Number:10
# Enter Second Number:20
# Enter Second Number:30
# Biggest number is: 30
# Enter First Number:30
# Enter Second Number:20
# Enter Second Number:10
# Biggest number is: 30
