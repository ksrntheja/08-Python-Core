g = (x * x for x in range(1000000000))
print(g)
print('type(g)', type(g))
while True:
    print(next(g))

# No hang
