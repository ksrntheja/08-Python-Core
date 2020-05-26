s = input('Enter a String to reverse:')

print('Using Slicing []')
print(s[::-1])

print()

print('Using reversed in-built function:')
r = reversed(s)
print('type(r)->', type(r))
output = ''.join(r)
print(output)

print()

print('Using while loop:')
i = len(s) - 1
output = ''
while i >= 0:
    output = output + s[i]
    i = i - 1
print(output)

# Enter a String to reverse:Theja
# Using Slicing []
# ajehT
#
# Using reversed in-built function:
# type(r)-> <class 'reversed'>
# ajehT
#
# Using while loop:
# ajehT
