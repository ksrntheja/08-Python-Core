s = input('Enter list:')
print(s)
print(type(s))

print()

l = eval(input('Enter list:'))
print(l)
print(type(l))

# Enter list:[10, 20, 30 , 40]
# [10, 20, 30 , 40]
# <class 'str'>

# Enter list:Hello
# Traceback (most recent call last):
#   File "/Code/venv/list/03Input.py", line <>, in <module>
#     l = eval(input('Enter list:'))
#   File "<string>", line <>, in <module>
# NameError: name 'Hello' is not defined

# Enter list:[10, 20, 30 , 40]
# [10, 20, 30 , 40]
# <class 'str'>
#
# Enter list:[10, 20, 30 , 40]
# [10, 20, 30, 40]
# <class 'list'>
