d = {100: 'A', 200: 'B', 300: 'C'}
print(d.get(100))
print(d.get(700))
print(d.get(100, "Default"))
print(d.get(700, "Default"))

# A
# None
# A
# Default
