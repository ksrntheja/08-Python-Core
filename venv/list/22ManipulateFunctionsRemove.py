n = [1, 2, 2, 2, 2, 3, 3]
x = int(input('Enter element to remove:'))
while True:
    if x in n:
        n.remove(x)
    else:
        break
print(n)

# Enter element to remove:1
# [2, 2, 2, 2, 3, 3]

# Enter element to remove:2
# [1, 3, 3]
