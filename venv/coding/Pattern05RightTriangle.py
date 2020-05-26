n = int(input('Enter N:'))

for i in range(n):
    print('* ' * (i + 1))

# Enter N:5
# A A A A A
# B B B B B
# C C C C C
# D D D D D
# E E E E E

# For print('* ' * i + 1)
# Enter N:5
# Traceback (most recent call last):
#   File "/Code/venv/coding/Pattern05RightTriangle.py", line <>, in <module>
#     print('* ' * i + 1)
# TypeError: must be str, not int
