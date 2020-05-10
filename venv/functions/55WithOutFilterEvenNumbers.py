def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False


l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1 = []
for i in l:
    if isEven(i):
        l1.append(i)
print(l1)

# [0, 2, 4, 6, 8, 10]
