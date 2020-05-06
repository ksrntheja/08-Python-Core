d = {100: 'A', 200: 'B', 300: 'C'}
items = d.items()
print(items, type(items))
for item in items:
    print(item, type(item))

# dict_items([(100, 'A'), (200, 'B'), (300, 'C')]) <class 'dict_items'>
# (100, 'A') <class 'tuple'>
# (200, 'B') <class 'tuple'>
# (300, 'C') <class 'tuple'>
