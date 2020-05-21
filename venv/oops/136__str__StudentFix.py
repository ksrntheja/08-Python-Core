class Student:

    def __init__(self, name, rollNo, marks):
        self.name = name
        self.rollNo = rollNo
        self.marks = marks

    def __str__(self):
        return 'Name:{}, RollNo:{}, Marks:{}'.format(self.name, self.rollNo, self.marks)


student01 = Student('Theja', 101, 100)
student02 = Student('ksrn', 102, 90)

print(student01)
print(student02)

# Name:Theja, RollNo:101, Marks:100
# Name:ksrn, RollNo:102, Marks:90
