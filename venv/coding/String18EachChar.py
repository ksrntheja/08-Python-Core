s = input('Enter String:')

print('Using list')
l = []
for ch in s:
    if ch not in l:
        l.append(ch)
for ch in sorted(l):
    print('{} occurs {} times'.format(ch, s.count(ch)))

print('Using set')
set = set(s)
for ch in sorted(set):
    print('{} occurs {} times'.format(ch, s.count(ch)))

print('Using dict')
d = {}
for ch in s:
    d[ch] = d.get(ch, 0) + 1
print('Using without sorted')
for k, v in d.items():
    print('{} occurs {} times'.format(k, v))
print('Using sorted')
for k, v in sorted(d.items()):
    print('{} occurs {} times'.format(k, v))

# Enter String:ABCDABXXXBCDABBBBCCCZZZZCDDDDEEEEEF
# Using list
# A occurs 3 times
# B occurs 7 times
# C occurs 6 times
# D occurs 6 times
# E occurs 5 times
# F occurs 1 times
# X occurs 3 times
# Z occurs 4 times
# Using set
# A occurs 3 times
# B occurs 7 times
# C occurs 6 times
# D occurs 6 times
# E occurs 5 times
# F occurs 1 times
# X occurs 3 times
# Z occurs 4 times
# Using dict
# Using without sorted
# A occurs 3 times
# B occurs 7 times
# C occurs 6 times
# D occurs 6 times
# X occurs 3 times
# Z occurs 4 times
# E occurs 5 times
# F occurs 1 times
# Using sorted
# A occurs 3 times
# B occurs 7 times
# C occurs 6 times
# D occurs 6 times
# E occurs 5 times
# F occurs 1 times
# X occurs 3 times
# Z occurs 4 times
