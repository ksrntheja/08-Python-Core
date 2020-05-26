s = input('Enter Some String where alphabet symbol should be followed by digit:')
output = ''
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output = output + x * d
print(''.join(sorted(output)))

# Enter Some String where alphabet symbol should be followed by digit:a3z2b4
# aaabbbbzz
