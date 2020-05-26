def fibonacci():
    prev, present = 0, 1
    while True:
        yield prev
        prev, present = present, prev + present


values = fibonacci()
for x in values:
    if x > 100:
        break
    print(x)

# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
