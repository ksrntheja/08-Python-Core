s = input('Enter Some String where alphabet symbol should be followed by digit:')
for ch in s:
    if ch.isalpha():
        print(ch * int(s[(s.index(ch) + 1)]), end='')

# Enter Some String where alphabet symbol should be followed by digit:a1b1c1
# abc
