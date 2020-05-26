def firstNValues(n):
    i = 1
    while i <= n:
        yield i
        i = i + 1


n = int(input('Enter N:'))
values = firstNValues(n)
for x in values:
    print(x)

# Enter N:5
# 1
# 2
# 3
# 4
# 5
