def hello(user):
    print('Hello {}'.format(user))


hello(input('Enter name: '))
hello(input('Enter name: '))
# hello(10, 20)
# TypeError: hello() takes 1 positional argument but 2 were given
hello()

# Enter name: Theja
# Hello Theja
# Enter name: KSRN
# Hello KSRN
# Traceback (most recent call last):
#   File "/Code/venv/functions/04HelloUser.py", line <>, in <module>
#     hello()
# TypeError: hello() missing 1 required positional argument: 'user'
