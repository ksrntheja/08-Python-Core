print('2        * "theja"   -> ', 2 * "theja")
print('"theja"  * 2         -> ', "theja" * 2)
print('"theja"  * int(2.5)  -> ', "theja" * int(2.5))

# print('"theja"  * 2.5       -> ', "theja" * 2.5)
# Traceback (most recent call last):
#   File "/Code/venv/operators/01arithmetic/07*ForStrings.py", line <>, in <module>
#     print('"theja"  * 2.5       -> ', "theja" * 2.5)
# TypeError: can't multiply sequence by non-int of type 'float'

print('"theja"  * "ksrn"    -> ', "theja" * "ksrn")

# 2        * "theja"   ->  thejatheja
# "theja"  * 2         ->  thejatheja
# "theja"  * int(2.5)  ->  thejatheja
# Traceback (most recent call last):
#   File "/Code/venv/operators/01arithmetic/07*ForStrings.py", line <>, in <module>
#     print('"theja"  * "ksrn"    -> ', "theja" * "ksrn")
# TypeError: can't multiply sequence by non-int of type 'str'
