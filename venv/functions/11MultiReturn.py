def sum_sub(a, b):
    sum = a + b
    sub = a - b
    return sum, sub


a = 10
b = 20
sum, sub = sum_sub(a, b)
print('{} + {} is {}'.format(a, b, sum))
print('{} - {} is {}'.format(a, b, sub))

print()

print('{} & {}'.format(sum_sub(a, b)))

# 10 + 20 is 30
# 10 - 20 is -10
#
# Traceback (most recent call last):
#   File "/Code/venv/functions/11MultiReturn.py", line <>, in <module>
#     print('{} & {}'.format(sum_sub(a, b)))
# IndexError: tuple index out of range
