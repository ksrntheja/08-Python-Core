s = {10, 20, 30, 40}
print(s, type(s))

s = {}
print(s, type(s))

s = set()
print(s, type(s))

s = set('thejaji,')
print(s, type(s))

l = ['the', 'ja', 'th', 'the', ]
s = set(l)
print(s, type(s))

t = ('the', 'ja', 'th', 'the',)
s = set(t)
print(s, type(s))

s = set(range(0, 101, 10))
print(s, type(s))

s = set(input(('Enter set :')))
print(s, type(s))

s = eval(input(('Enter set :')))
print(s, type(s))

# {40, 10, 20, 30} <class 'set'>
# {} <class 'dict'>
# set() <class 'set'>
# {',', 'e', 'a', 't', 'j', 'h', 'i'} <class 'set'>
# {'th', 'the', 'ja'} <class 'set'>
# {'th', 'the', 'ja'} <class 'set'>
# {0, 100, 70, 40, 10, 80, 50, 20, 90, 60, 30} <class 'set'>
# Enter set :{10, 20, 10}
# {'2', ',', '0', '1', '}', '{', ' '} <class 'set'>
# Enter set :{10, 20, 10}
# {10, 20} <class 'set'>
