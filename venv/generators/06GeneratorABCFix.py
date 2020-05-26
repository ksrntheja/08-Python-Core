def myGen():
    yield 'A'
    yield 'B'
    yield 'C'


g = myGen()
print(type(g))

for x in g:
    print(x)

# <class 'generator'>
# A
# B
# C
