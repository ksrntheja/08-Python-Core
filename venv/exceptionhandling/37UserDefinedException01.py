class TooYoungException(Exception):
    def __init__(self, arg):
        self.msg = arg


class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg


age = int(input("Enter Age:"))
if age > 60:
    raise TooYoungException("Plz wait some more time you will get best match soon!!!")
elif age < 18:
    # raise TooOldException()
    # Traceback (most recent call last):
    #   File "/Code/venv/exceptionhandling/37UserDefinedException01.py", line <>, in <module>
    #     raise TooOldException()
    # TypeError: __init__() missing 1 required positional argument: 'arg'
    raise TooOldException("Your age already crossed marriage age...no chance of getting marriage")
else:
    print("You will get match details soon by email!!!")

# Enter Age:12
# Traceback (most recent call last):
#   File "/Code/venv/exceptionhandling/37UserDefinedException01.py", line 20, in <module>
#     raise TooOldException("Your age already crossed marriage age...no chance of getting marriage")
# __main__.TooOldException: Your age already crossed marriage age...no chance of getting marriage

# Enter Age:100
# Traceback (most recent call last):
#   File "/Code/venv/exceptionhandling/37UserDefinedException01.py", line 13, in <module>
#     raise TooYoungException("Plz wait some more time you will get best match soon!!!")
# __main__.TooYoungException: Plz wait some more time you will get best match soon!!!

# Enter Age:30
# You will get match details soon by email!!!
