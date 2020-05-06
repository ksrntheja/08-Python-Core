x = eval(input('Enter:'))
print(type(x))
print(x)

# Enter:10
# <class 'int'>
# Enter:10.5
# <class 'float'>
# Enter:True
# <class 'bool'>
# Enter:[10, 20, 30]
# <class 'list'>
# Enter:(10, 20, 30)
# <class 'tuple'>
# Enter:(10)
# <class 'int'>
# Enter:(10,)
# <class 'tuple'>
#  Enter:10 + 20 + 30
# <class 'int'>
# 60
# Enter:10+20/3**4//5*40
# <class 'float'>
# 10.0
# Enter:Theja
# Traceback (most recent call last):
#   File "/Code/venv/inputoutputfunctions/09EvalDemo.py", line <>, in <module>
#     x = eval(input('Enter:'))
#   File "<string>", line <>, in <module>
# NameError: name 'Theja' is not defined
