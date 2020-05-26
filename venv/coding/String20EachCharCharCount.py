s = input('Enter String:')

d = {}
output = ''
for ch in s:
    d[ch] = d.get(ch, 0) + 1

for k, v in d.items():
    output = output + k + str(v)
print(output)

# Enter String:ABAABBCA
# A4B3C1
