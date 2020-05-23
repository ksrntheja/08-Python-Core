class TooYoungException(Exception):
    pass


class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg


age = int(input("Enter Age:"))
if age > 60:
    raise ArithmeticError("Plz wait some more time you will get best match soon!!!")
elif age < 18:
    raise TooOldException("Your age already crossed marriage age...no chance of getting marriage")
else:
    print("You will get match details soon by email!!!")

# Enter Age:100
# Traceback (most recent call last):
#   File "/Code/venv/exceptionhandling/39UserDefinedException03.py", line 12, in <module>
#     raise ArithmeticError("Plz wait some more time you will get best match soon!!!")
# ArithmeticError: Plz wait some more time you will get best match soon!!!
