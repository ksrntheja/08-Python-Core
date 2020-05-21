class Account:
    def __init__(self, initial_balance):
        self.__balance = initial_balance

    def getBalance(self):
        # Validation
        return self.__balance


a = Account(10000)
# print(a.__balance)
print(a.getBalance())

# 10000
