l = [x for x in range(1, 11)]
print(l)

s = 'AAAAABBBAAABBA'
l = [x for x in s if x == 'B']
print(l)

s = [x * x for x in range(1, 11)]
print(s)
v = [2 ** x for x in range(1, 6)]
print(v)
m = [x for x in s if x % 2 == 0]
print(m)

l = [x for x in range(1, 101) if x % 10 == 0]
print(l)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ['B', 'B', 'B', 'B', 'B']
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [2, 4, 8, 16, 32]
# [4, 16, 36, 64, 100]
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
