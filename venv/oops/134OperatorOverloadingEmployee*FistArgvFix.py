class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class TimeSheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days

    def __mul__(self, other):
        return self.days * other.salary


e = Employee('Theja', 500)
t = TimeSheet('Theja', 25)
print('This Month Salary:', t * e)

# This Month Salary: 12500
