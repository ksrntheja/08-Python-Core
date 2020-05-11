from random import *

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWZXY'
# city = ['AA', 'BB', 'CC', 'DD', 'EE', 'FF']
# TypeError: object of type 'function' has no len()
cities = ['AA', 'BB', 'CC', 'DD', 'EE', 'FF']


def name():
    # name - 3 to 10 characters, Capitalize case
    name = ''
    for i in range(1, randint(4, 10)):
        name = name + choice(alphabets)
    return name.capitalize()


def eNumber():
    # eNumber - start with 'e-4 digits'
    eNumber = 'e-'
    for i in range(4):
        eNumber = eNumber + str(randint(0, 9))
    return eNumber


def sal():
    # sal - Float from 10000 to 50000
    sal = uniform(9999, 50001)
    return sal


def city():
    # city - From - ['AA', 'BB', 'CC', 'DD', 'EE', 'FF']
    return choice(cities)


def mobile():
    # mobile - start with 6 to 9 and 10 digits
    mobile = str(randint(6, 9))
    for i in range(9):
        mobile = mobile + str(randint(0, 9))
    return mobile


def emp():
    print(name())
    print(eNumber())
    print('{:.2f}'.format(sal()))
    print(city())
    print(mobile())


emp()

# Bwagjqik
# e-9945
# 46582.73
# AA
# 7141789262
