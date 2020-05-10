def evenOdd(number):
    if number % 2 == 0:
        return "even"
    return "odd"


number = int(input('Enter a number: '))
print('{} is {}'.format(number, evenOdd(number)))

# Enter a number: 2
# 2 is even


# Enter a number: 1
# 1 is odd
