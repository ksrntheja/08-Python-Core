x = 10
if x > 10:
    print('x > 10')
else:
    print('x <= 10')
print()
for x in range(10):
    print('The current value of x', x)
else:
    print('No break in loop')
print()
for x in range(10):
    if x > 5:
        break
    print('The current value of x', x)
else:
    print('No break in loop')
