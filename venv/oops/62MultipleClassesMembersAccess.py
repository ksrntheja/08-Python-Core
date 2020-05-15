class Employee:
    def __init__(self, eno, ename, esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal

    def display(self):
        print('Employee Number:', self.eno)
        print('Employee Name:', self.ename)
        print('Employee Salary:', self.esal)


class Test:
    def modify(emp):
        # Static method : Assume emp as 'self', Test does not have esal and display() method
        # Assumption of emp as 'self' is wrong. So it is static method
        emp.esal = emp.esal + 10000
        emp.display()


e = Employee(100, 'Theja', 10000)
e.display()
print()
Test.modify(e)

# Employee Number: 100
# Employee Name: Theja
# Employee Salary: 10000
#
# Employee Number: 100
# Employee Name: Theja
# Employee Salary: 20000
