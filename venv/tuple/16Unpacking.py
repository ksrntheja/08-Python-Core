t = (10, 20, 30, 40)
a, b, c, d = t
print("a=", a, "b=", b, "c=", c, "d=", d)

t = (10, 20, 30, 40)

# a, b, c = t
# a= 10 b= 20 c= 30 d= 40
# Traceback (most recent call last):
#   File "/Code/venv/tuple/16Unpacking.py", line <>, in <module>
#     a, b, c = t
# ValueError: too many values to unpack (expected 3)

a, b, c, d, e = t

# a= 10 b= 20 c= 30 d= 40
# Traceback (most recent call last):
#   File "Code/venv/tuple/16Unpacking.py", line <>, in <module>
#     a, b, c, d, e = t
# ValueError: not enough values to unpack (expected 5, got 4)
