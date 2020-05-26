s = input('Enter String:')

d = {}
output = ''
for ch in s:
    d[ch] = d.get(ch, 0) + 1

for k, v in d.items():
    output = output + str(v) + k
print(output)

# Enter String:ABAABBCA
# 4A3B1C
