import math
from math import sqrt as sq

print(math.frexp(10.5))
print(math.floor(10.5))
print(math.fabs(-10.5))
print(math.fmod(10.5, 6))
print(math.ceil(10.5))

print()

print(math.sqrt(4))
print(sq(4))

print()

l = [str(round(math.pi)) for i in range(1, 6)]
print(l)

print()

print('round(10.999) ->', round(10.999))
print('round(10.51)  ->', round(10.51))
print('round(10.50)  ->', round(10.50))
print('round(10.49)  ->', round(10.49))

print()


def find_area(r):
    return math.pi * math.pow(r, 2)


print('Area of circle having r = 2 ->', find_area(2))

# (0.65625, 4)
# 10
# 10.5
# 4.5
# 11
#
# 2.0
# 2.0
#
# ['3', '3', '3', '3', '3']
#
# round(10.999) -> 11
# round(10.51)  -> 11
# round(10.50)  -> 10
# round(10.49)  -> 10
#
# Area of circle having r = 2 -> 12.566370614359172
