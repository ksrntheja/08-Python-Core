d = {100: 'A', 200: 'B', 300: 'C'}
print(d)
print(d.pop(200, 'Guest'))
print(d)
print(d.pop(800, 'Guest'))
print(d)

# {100: 'A', 200: 'B', 300: 'C'}
# B
# {100: 'A', 300: 'C'}
# Guest
# {100: 'A', 300: 'C'}
