number = int(input('Enter a number:'))
if number < 2:
    print('No primes')
else:
    primes = []
    for num in range(2, number + 1):
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
    print(primes)

# Enter a number:8
# [2, 3, 5, 7]
