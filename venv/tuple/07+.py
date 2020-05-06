t1 = (10, 20, 30)
t2 = (40, 50, 60)
t3 = t1 + t2
print(t3)
print(t1)
print(t2)

# t3 = t1 + 10
# Traceback (most recent call last):
#   File "/Code/venv/tuple/07+.py", line <>, in <module>
#     t3 = t1 + 10
# TypeError: can only concatenate tuple (not "int") to tuple

t3 = t1 + [10]

# (10, 20, 30, 40, 50, 60)
# (10, 20, 30)
# (40, 50, 60)
# Traceback (most recent call last):
#   File "/Code/venv/tuple/07+.py", line <>, in <module>
#     t3 = t1 + [10]
# TypeError: can only concatenate tuple (not "list") to tuple
