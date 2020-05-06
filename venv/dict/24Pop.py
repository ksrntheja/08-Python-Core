d = {100: 'A', 200: 'B', 300: 'C'}
print(d)
print(d.pop(200))
print(d)
print(d.pop(800))

# {100: 'A', 200: 'B', 300: 'C'}
# B
# {100: 'A', 300: 'C'}
# Traceback (most recent call last):
#   File "/Code/venv/dict/24Pop.py", line <>, in <module>
#     print(d.pop(800))
# KeyError: 800
