def square(number):
    print('Sqaure of {} is {}'.format(number, number * number))


# square((input('Enter number: ')))
# TypeError: can't multiply sequence by non-int of type 'str'
square(eval(input('Enter number: ')))
square(eval(input('Enter number: ')))

# Enter number: 1
# Sqaure of 1 is 1
# Enter number: 2
# Sqaure of 2 is 4
