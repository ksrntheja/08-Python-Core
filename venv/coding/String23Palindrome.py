s = input("Enter string:")
print(reversed(s))
print(''.join(reversed(s)))
if s == ''.join(reversed(s)):
    print("The strings are palindromes.")
else:
    print("The strings aren't palindromes.")

# Enter string:madam
# <reversed object at 0x7f8c912c8da0>
# madam
# The strings are palindromes.

# Enter string:Madam
# <reversed object at 0x7fe7b83bada0>
# madaM
# The strings aren't palindromes.
