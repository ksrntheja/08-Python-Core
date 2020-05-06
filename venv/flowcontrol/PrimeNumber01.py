number = int(input('Enter a number:'))
if number < 2:
    print(number, 'is not prime')
else:
    is_prime = False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            break
    else:
        is_prime = True
    print(number, 'is prime' if is_prime else 'is not prime')

# Enter a number:8
# 8 is not prime
# Enter a number:89
# 89 is prime
