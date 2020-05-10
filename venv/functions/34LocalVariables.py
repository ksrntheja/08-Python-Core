def f01():
    a = 10
    print(a)


def f02():
    print(a)


f01()
f02()

# 10
# Traceback (most recent call last):
#   File "/Code/venv/functions/34LocalVariables.py", line <>, in <module>
#     f02()
#   File "/Code/venv/functions/34LocalVariables.py", line <>, in f02
#     print(a)
# NameError: name 'a' is not defined
