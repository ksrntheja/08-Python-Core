def wish(name):
    print("Good Morning:", name)


greeting = wish
greeting('Theja')
wish('Theja')

del greeting
# greeting('Hello')
# Traceback (most recent call last):
#   File "/Code/venv/functions/71FunctionAliasingDelete01.py", line <>, in <module>
#     greeting('Hello')
# NameError: name 'greeting' is not defined
wish('Hello')

# Good Morning: Theja
# Good Morning: Theja
# Good Morning: Hello
