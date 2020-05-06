d = {}
l = [10, 20, 30]
t = (100, 200, 100, 10)
d[t] = 'A'
print(d)
d[l] = 'B'

# {(100, 200, 100, 10): 'A'}
# Traceback (most recent call last):
#   File "/Code/venv/tuple/21Add TupleToDict.py", line <>, in <module>
#     d[l] = 'B'
# TypeError: unhashable type: 'list'
