a = 10
b = 20

print('a = ', a)
print('b = ', b)

print("a >  b   is ", a > b)
print("a >= b   is ", a >= b)
print("a <  b   is ", a < b)
print("a <= b   is ", a <= b)

print("a < '10' is ", a <= '10')

# a =  10
# b =  20
# a >  b   is  False
# a >= b   is  False
# a <  b   is  True
# a <= b   is  True
# Traceback (most recent call last):
#   File "/Code/venv/operators/02relational/01RelationalOperators.py", line <>, in <module>
#     print("a < '10' is ", a <= '10')
# TypeError: '<=' not supported between instances of 'int' and 'str'
