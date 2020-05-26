s1 = input('Enter first  String:')
s2 = input('Enter second String:')

i, j = 0, 0
output = ''
while i < len(s1) or j < len(s2):
    output = output + s1[i] + s2[j]
    i = i + 1
    j = j + 1
print(output)

# Enter first  String:Four
# Enter second String:Five
# FFoiuvre

# Enter first  String:One
# Enter second String:Three
# Traceback (most recent call last):
#   File "/Code/venv/coding/String07Merge2StringsAlternatively.py", line 7, in <module>
#     output = output + s1[i] + s2[j]
# IndexError: string index out of range
