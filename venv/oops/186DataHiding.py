class Account:
    def __init__(self, initial_balance):
        self.__balance = initial_balance


a = Account(10000)
print(a.__balance)

# Traceback (most recent call last):
#   File "/Code/venv/oops/186DataHiding.py", line <>, in <module>
#     print(a.__balance)
# AttributeError: 'Account' object has no attribute '__balance'
