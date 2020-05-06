print('4    & 5    -> ', 4 & 5)
print('4    & -1   -> ', 4 & -5)

print('4    | 5    -> ', 4 | 5)
print('4    ^ 5    -> ', 4 ^ 5)

print('True  & True  -> ', True & True)
print('True  & False -> ', True & False)
print('False & True  -> ', False & True)
print('False & False -> ', False & False)

print('True  | True  -> ', True | True)
print('True  | False -> ', True | False)
print('False | True  -> ', False | True)
print('False | False -> ', False | False)

print('True  ^ True  -> ', True ^ True)
print('True  ^ False -> ', True ^ False)
print('False ^ True  -> ', False ^ True)
print('False ^ False -> ', False ^ False)

print('True  << True  -> ', True << True)
print('True  << False -> ', True << False)
print('False << True  -> ', False << True)
print('False << False -> ', False << False)

print('True  >> True  -> ', True >> True)
print('True  >> False -> ', True >> False)
print('False >> True  -> ', False >> True)
print('False >> False -> ', False >> False)

# print('True ~ True  -> ', True ~ True)
#   File "/Code/venv/operators/05bitwise/01BitwiseOperators.py", line <>
#     print('True ~ True  -> ', True ~ True)
#                                     ^
# SyntaxError: invalid syntax

print()

# print('10.5 & 5 -> ', 10.5 & 5)
# Traceback (most recent call last):
#   File "/Code/venv/operators/05bitwise/01BitwiseOperators.py", line <>, in <module>
#     print('10.5 & 5 -> ', 10.5 & 5)
# TypeError: unsupported operand type(s) for &: 'float' and 'int'

print('"10.5" & 5 -> ', "10" & 5)

# 4    & 5    ->  4
# 4    & -1   ->  0
# 4    | 5    ->  5
# 4    ^ 5    ->  1
# True  & True  ->  True
# True  & False ->  False
# False & True  ->  False
# False & False ->  False
# True  | True  ->  True
# True  | False ->  True
# False | True  ->  True
# False | False ->  False
# True  ^ True  ->  False
# True  ^ False ->  True
# False ^ True  ->  True
# False ^ False ->  False
# True  << True  ->  2
# True  << False ->  1
# False << True  ->  0
# False << False ->  0
# True  >> True  ->  0
# True  >> False ->  1
# False >> True  ->  0
# False >> False ->  0
#
# Traceback (most recent call last):
#   File "/Code/venv/operators/05bitwise/01BitwiseOperators.py", line <>, in <module>
#     print('"10.5" & 5 -> ', "10" & 5)
# TypeError: unsupported operand type(s) for &: 'str' and 'int'
