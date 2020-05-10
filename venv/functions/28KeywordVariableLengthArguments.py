def var(**n):
    print('Printing n :', n, 'type of n :', type(n))


var()
print()
var(name='Theja', rollNo=101)
print()
var(A=10, B=20, C=30)
print()
sk = 'Hello'
sv = 'HelloValue'
var(sk=sv)
print()
tk = (10, 20)
tv = (30, 40)
var(tk=tv)
print()

# var(10=100, 20=200, 30=300)
#   File "/Code/venv/functions/28KeywordVariableLengthArguments.py", line <>
#     var(10=100, 20=200, 30=300)
#        ^
# SyntaxError: keyword can't be an expression
# var(10='100', 20='200', 30='300')
#   File "/Code/venv/functions/28KeywordVariableLengthArguments.py", line <>
#     var(10='100', 20='200', 30='300')
#        ^
# SyntaxError: keyword can't be an expression

d = {10: 20, 30: 40}
print(d, type(d))
d = {10: '20', 30: '40'}
print(d, type(d))

# Printing n : {} type of n : <class 'dict'>
#
# Printing n : {'name': 'Theja', 'rollNo': 101} type of n : <class 'dict'>
#
# Printing n : {'A': 10, 'B': 20, 'C': 30} type of n : <class 'dict'>
#
# Printing n : {'sk': 'HelloValue'} type of n : <class 'dict'>
#
# Printing n : {'tk': (30, 40)} type of n : <class 'dict'>
#
# {10: 20, 30: 40} <class 'dict'>
# {10: '20', 30: '40'} <class 'dict'>
