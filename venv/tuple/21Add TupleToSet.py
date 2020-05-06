s = {10, 20}
l = [10, 20, 30]
t = (100, 200, 100, 10)
# s.add(l)
# Traceback (most recent call last):
#   File "/Code/venv/tuple/21Add TupleToSet.py", line <>, in <module>
#     s.add(l)
# TypeError: unhashable type: 'list'
s.add(t)
print(s)

# {(100, 200, 100, 10), 10, 20}
