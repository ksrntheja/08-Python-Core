print('stmt-1')
try:
    print(10 / 0)
except ZeroDivisionError:
    print(10 / 2)
print('stmt-3')

# stmt-1
# 5.0
# stmt-3
