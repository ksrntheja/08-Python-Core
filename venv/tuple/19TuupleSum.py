t = eval(input('Enter tuple:'))
sum = 0
for x in t:
    sum += x
print('Sum -> ', sum)
print('Avg -> ', sum / len(t))

# Enter tuple:10, 20, 30, 40
# Sum ->  100
# Avg ->  25.0

# Enter tuple:100, 200, 300
# Sum ->  600
# Avg ->  200.0
