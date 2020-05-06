t = (10, 20, 30, 40)
print(len(t))

t = (10, 20, 10, 10, 20)
print(t.count(10))

t = (10, 20, 10, 10, 20)
print(t.index(10))
print(t.index(30))

# 4
# 3
# 0
# Traceback (most recent call last):
#   File "/Code/venv/tuple/12Functions-01.py", line <>, in <module>
#     print(t.index(30))
# ValueError: tuple.index(x): x not in tuple
