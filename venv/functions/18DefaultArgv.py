def wish(name):
    print("Hello", name, "Good Morning")


wish("Theja")
wish()

# Hello Theja Good Morning
# Traceback (most recent call last):
#   File "/Code/venv/functions/18DefaultArgv.py", line <>, in <module>
#     wish()
# TypeError: wish() missing 1 required positional argument: 'name'
