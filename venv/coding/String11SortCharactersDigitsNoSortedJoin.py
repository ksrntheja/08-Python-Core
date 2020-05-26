s = input('Enter a String:')
alphabets = ''
digits = ''
for ch in s:
    if ch.isalpha():
        alphabets += ch
    else:
        digits += ch
output = ''
for ch in sorted(alphabets):
    output = output + ch
for ch in sorted(digits):
    output = output + ch
print(output)

# Enter a String:1One2Two3Th4
# OTTehnow1234
