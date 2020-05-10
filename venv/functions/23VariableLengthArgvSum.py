def sum(*n):
    sum = 0
    for number in n:
        sum += number
    print('Sum ->', sum)


sum()
sum(1)
sum(1, 2)

# Sum -> 0
# Sum -> 1
# Sum -> 3
