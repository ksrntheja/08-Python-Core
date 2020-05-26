s = input('Enter a String:')
print(sorted(s))
print(sorted(s, reverse=True))
alphabets = []
digits = []
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        digits.append(ch)
output = ''.join(sorted(alphabets) + sorted(digits))
print(output)

# Enter a String:1One2Two3Th4
# ['1', '2', '3', '4', 'O', 'T', 'T', 'e', 'h', 'n', 'o', 'w']
# ['w', 'o', 'n', 'h', 'e', 'T', 'T', 'O', '4', '3', '2', '1']
# OTTehnow1234
