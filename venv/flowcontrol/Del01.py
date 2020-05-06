# print(x) - NameError
x = 10
print(x)
del x
print(x)

# 10
# Traceback (most recent call last):
#   File "/Code/venv/flowcontrol/Del01.py", line <>, in <module>
#     print(x)
# NameError: name 'x' is not defined
