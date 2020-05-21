class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('Name:', self.name)
        print('Age:', self.age)


class Employee(Person):
    def __init__(self, name, age, eno, esal):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal

    def display(self):
        # super(Employee, self).display()
        super().display()
        print("Employee Number:", self.eno)
        print("Employee Salary:", self.esal)


e = Employee('Theja', 50, 500, 5000)
e.display()

# Name: Theja
# Age: 50
# Employee Number: 500
# Employee Salary: 5000
