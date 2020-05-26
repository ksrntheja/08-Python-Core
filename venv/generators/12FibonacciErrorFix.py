def fibonacci(n):
    prev, present = 0, 1
    i = 0
    while i < n:
        yield prev
        future = prev + present
        prev = present
        present = future
        i = i + 1


n = int(input('Enter N:'))
values = fibonacci(n)
for x in values:
    print(x)

# Enter N:5
# 0
# 1
# 1
# 2
# 3
