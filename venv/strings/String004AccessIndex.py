s = input('Enter string:')
i = 0
for x in s:
    print('The character present at Positive Index {} and'
          ' Negative Index {} is {}'.format(i, i - len(s), x))
    i += 1

# Enter string:theja
# The character present at Positive Index 0 and Negative Index -5 is t
# The character present at Positive Index 1 and Negative Index -4 is h
# The character present at Positive Index 2 and Negative Index -3 is e
# The character present at Positive Index 3 and Negative Index -2 is j
# The character present at Positive Index 4 and Negative Index -1 is a
