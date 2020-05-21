class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other):
        return self.salary * other.days


class TimeSheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days


e = Employee('Theja', 500)
t = TimeSheet('Theja', 25)
print('This Month Salary:', t * e)

# Traceback (most recent call last):
#   File "/Code/venv/oops/133OperatorOverloadingEmployee*FistArgv.py", line <>, in <module>
#     print('This Month Salary:', t * e)
# TypeError: unsupported operand type(s) for *: 'TimeSheet' and 'Employee'
