number = int(input('Enter a number:'))
primes = []
num = 2
while len(primes) < number:
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            break
    else:
        primes.append(num)
    num += 1
print(primes)

# Enter a number:8
# [2, 3, 5, 7, 11, 13, 17, 19]
