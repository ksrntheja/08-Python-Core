class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks

    def __str__(self):
        return 'Name={}\nAge={}\nRollno={}\nMarks={}'.format(self.name, self.age, self.rollno, self.marks)


s = Student('theja', 50, 100, 150)
print(s)

# Name=theja
# Age=50
# Rollno=100
# Marks=150
