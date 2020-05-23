class TooYoungException(Exception):
    pass


class TooOldException(Exception):
    def __init__(self, hello):
        self.hello = hello


age = int(input("Enter Age:"))
if age > 60:
    raise ArithmeticError("Plz wait some more time you will get best match soon!!!")
elif age < 18:
    raise TooOldException("Your age already crossed marriage age...no chance of getting marriage")
else:
    print("You will get match details soon by email!!!")

# Enter Age:12
# Traceback (most recent call last):
#   File "/Code/venv/exceptionhandling/41UserDefinedException05.py", line 14, in <module>
#     raise TooOldException("Your age already crossed marriage age...no chance of getting marriage")
# __main__.TooOldException: Your age already crossed marriage age...no chance of getting marriage
