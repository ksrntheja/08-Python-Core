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


e1 = Employee('Theja', 500)
t = TimeSheet('Theja', 25)
print('This Month Salary:', e1 * t)
e2 = Employee('Theja', 500)
print('This Month Salary:', e1 * e2)

# This Month Salary: 12500
# Traceback (most recent call last):
#   File "/Code/venv/oops/132OperatorOverloadingEmployee*.py", line <>, in <module>
#     print('This Month Salary:', e1 * e2)
#   File "/Code/venv/oops/132OperatorOverloadingEmployee*.py", line <>, in __mul__
#     return self.salary * other.days
# AttributeError: 'Employee' object has no attribute 'days'
