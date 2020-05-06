t = (x ** 2 for x in range(1, 11))
print(t, type(t))
for x in t:
    print(x, type(x))

# <generator object <genexpr> at 0x7f935edb8e08> <class 'generator'>
# 1 <class 'int'>
# 4 <class 'int'>
# 9 <class 'int'>
# 16 <class 'int'>
# 25 <class 'int'>
# 36 <class 'int'>
# 49 <class 'int'>
# 64 <class 'int'>
# 81 <class 'int'>
# 100 <class 'int'>
