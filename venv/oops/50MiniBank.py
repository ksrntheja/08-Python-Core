class Customer:
    """Bank demo doc string"""

    bankName = 'Theja Bank'  # Static variable

    def __init__(self, name, balance=0.0):  # = 0.0 Default argument
        self.name = name
        self.balance = balance

    def deposit(self, amount):  # Instance method
        self.balance += amount
        print('After deposit balance:', self.balance)
        print('def deposit(self, amount) start...')

    def withdraw(self, amount):  # Instance method
        if amount > self.balance:
            print('Insufficient Funds...')
        else:
            self.balance -= amount
            print('After withdrawal, Balance:', self.balance)


print('Welcome to', Customer.bankName)
name = input('Enter name:')
c = Customer(name)

while True:
    print('d-Deposit', 'w-withdraw', 'e-exit', sep='\n')
    option = input('Choose your option:')
    if option.lower() == 'd':
        amount = float(input('Enter amount:'))
        c.deposit(amount)
    elif option.lower() == 'w':
        amount = float(input('Enter amount:'))
        c.withdraw(amount)
    elif option.lower() == 'e':
        print('Thanks for banking')
        break
    else:
        print('Option invalid, Please choose valid option')

# Welcome to Theja Bank
# Enter name:KSRN Theja
# d-Deposit
# w-withdraw
# e-exit
# Choose your option:d
# Enter amount:10000
# After deposit balance: 10000.0
# def deposit(self, amount) start...
# d-Deposit
# w-withdraw
# e-exit
# Choose your option:20000
# Option invalid, Please choose valid option
# d-Deposit
# w-withdraw
# e-exit
# Choose your option:w
# Enter amount:10000
# After withdrawal, Balance: 0.0
# d-Deposit
# w-withdraw
# e-exit
# Choose your option:w
# Enter amount:10000000
# Insufficient Funds...
# d-Deposit
# w-withdraw
# e-exit
# Choose your option:Y
# Option invalid, Please choose valid option
# d-Deposit
# w-withdraw
# e-exit
# Choose your option:e
# Thanks for banking
