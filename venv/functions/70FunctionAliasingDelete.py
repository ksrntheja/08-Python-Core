def wish(name):
    print("Good Morning:", name)


greeting = wish
greeting('Theja')
wish('Theja')

del wish
# wish('Hello')
# Traceback (most recent call last):
#   File "Code/venv/functions/70FunctionAliasingDelete.py", line <>, in <module>
#     wish('Hello')
# NameError: name 'wish' is not defined
greeting('Hello')

# Good Morning: Theja
# Good Morning: Theja
# Good Morning: Hello
