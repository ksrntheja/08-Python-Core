g = (x * x for x in range(10))
print(g)
print('type(g)', type(g))
while True:
    print(next(g))

# <generator object <genexpr> at 0x7fb0b6250ca8>
# type(g) <class 'generator'>
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# Traceback (most recent call last):
#   File "/Code/venv/generators/03Generator.py", line <>, in <module>
#     print(next(g))
# StopIteration
