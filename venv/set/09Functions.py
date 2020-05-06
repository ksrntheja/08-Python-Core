s = {40, 10, 30, 20}
print(s, type(s))
print(s.remove(30))
print(s, type(s))
print(s.remove(50))

# {40, 10, 20, 30} <class 'set'>
# None
# {40, 10, 20} <class 'set'>
# Traceback (most recent call last):
#   File "/Code/venv/set/09Functions.py", line <>, in <module>
#     print(s.remove(50))
# KeyError: 50
