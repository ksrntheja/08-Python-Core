def myGen():
    yield 'A'
    yield 'B'
    yield 'C'


g = myGen()
print(type(g))

print(next(g))
print(next(g))
print(next(g))
print(next(g))

# <class 'generator'>
# A
# B
# C
# Traceback (most recent call last):
#   File "/Code/venv/generators/05GeneratorABC.py", line <>, in <module>
#     print(next(g))
# StopIteration
