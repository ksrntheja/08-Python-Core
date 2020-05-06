d = {100: 'A', 200: 'B', 300: 'C'}
key = int(input('Enter key to get value:'))
if key in d:
    print('The corresponding value:', d.get(key))
else:
    print('The specified key is not available')

# Enter key to get value:100
# The corresponding value: A

# Enter key to get value:800
# The specified key is not available
