def firstNValues(n):
    i = n
    while i > 0:
        yield i
        i = i - 1


n = int(input('Enter N:'))
values = firstNValues(n)
import time

for x in values:
    print(x)
    time.sleep(1)

# Enter N:5
# 5
# 4
# 3
# 2
# 1
