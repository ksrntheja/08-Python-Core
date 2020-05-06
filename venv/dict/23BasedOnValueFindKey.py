d = {100: 'A', 200: 'B', 300: 'C', 400: 'A'}
value = input('Enter value to get key:')
if value in d.values():
    for k, v in d.items():
        if value == v:
            print('The corresponding key:', k)
else:
    print('The specified value is not available')

# Enter value to get key:B
# The corresponding key: 200

# Enter value to get key:False
# The specified value is not available

# Enter value to get key:A
# The corresponding key: 100
# The corresponding key: 400
