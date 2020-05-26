s1 = input('Enter first  String:')
s2 = input('Enter second String:')

i, j = 0, 0
output = ''
while i < len(s1) or j < len(s2):
    if i < len(s1):
        output = output + s1[i]
        i = i + 1
    if j < len(s2):
        output = output + s2[j]
        j = j + 1
print(output)

# Enter first  String:One
# Enter second String:Three
# OTnheree
