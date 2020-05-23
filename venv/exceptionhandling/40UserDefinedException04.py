class TooYoungException(Exception):
    pass


class TooOldException(Exception):
    def __init__(self, arg):
        self.msg = arg


age = int(input("Enter Age:"))
if age > 60:
    raise ArithmeticError("Plz wait some more time you will get best match soon!!!")
elif age < 18:
    raise ThejaError("Your age already crossed marriage age...no chance of getting marriage")
else:
    print("You will get match details soon by email!!!")

# Enter Age:12
# Traceback (most recent call last):
#   File "/Code/venv/exceptionhandling/40UserDefinedException04.py", line <>, in <module>
#     raise ThejaError("Your age already crossed marriage age...no chance of getting marriage")
# NameError: name 'ThejaError' is not defined
