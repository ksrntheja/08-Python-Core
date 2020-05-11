from random import *


def otp():
    # otp = 0
    otp = ''
    for i in range(6):
        # otp = otp * 10 + randint(0, 9)
        otp = otp + str(randint(0, 9))
    return otp


print(otp())
print(randint(0, 9), randint(0, 9), randint(0, 9),
      randint(0, 9), randint(0, 9), randint(0, 9),
      sep='')
# print(randint(0, 9) * 6) 48
# print(randint(000000, 999999)) 50110
# print(randint(100000, 999999)) No start with 0
# print(str(randint(0, 9)) * 6) 333333

# 856434
# 590532
