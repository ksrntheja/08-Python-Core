d = {100: "theja", 200: "ravi", 300: "shiva", 400: "ram", 500: "sri"}
print(d)
del d[100]
print(d)
del d[200], d[400], d[500]
print(d)
del d[800]

# {100: 'theja', 200: 'ravi', 300: 'shiva', 400: 'ram', 500: 'sri'}
# {200: 'ravi', 300: 'shiva', 400: 'ram', 500: 'sri'}
# {300: 'shiva'}
# Traceback (most recent call last):
#   File "/Code/venv/dict/08Update.py", line <>, in <module>
#     del d[800]
# KeyError: 800
