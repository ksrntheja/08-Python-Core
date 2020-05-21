class Student:
    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo

    def __str__(self):
        return 'This is Student with Name:{} and Rollno:{}'.format(self.name, self.rollNo)


s1 = Student('Theja', 101)
s2 = Student('ksrn', 102)
print(s1)
print(s2)

# This is Student with Name:Theja and Rollno:101
# This is Student with Name:ksrn and Rollno:102
