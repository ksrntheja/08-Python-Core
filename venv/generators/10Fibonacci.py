def fibonacci(n):
    prev, present = 0, 1
    i = 0
    while i < n:
        yield prev
        prev, present = present, prev + present
        i = i + 1


n = int(input('Enter N:'))
values = fibonacci(n)
for x in values:
    print(x)

# Enter N:5
# 5
# 4
# 3
# 2
# 1
