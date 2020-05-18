class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('Name:', self.name)
        print('Age:', self.age)


class Student(Person):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks

    def display(self):
        super().display()
        print('Roll No:', self.rollno)
        print('Marks:', self.marks)


s = Student('theja', 50, 100, 150)
s.display()

# Name: theja
# Age: 50
# Roll No: 100
# Marks: 150
