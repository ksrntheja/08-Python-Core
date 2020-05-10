a = 10


def f01():
    print(a)
    a = 20
    print(a)


f01()

# Traceback (most recent call last):
#   File "/Code/venv/functions/41UnboundLocalError.py", line <>, in <module>
#     f01()
#   File "/Code/venv/functions/41UnboundLocalError.py", line <>, in f01
#     print(a)
# UnboundLocalError: local variable 'a' referenced before assignment
