class Student:
    """Demo student doc"""

    def __init__(self, name, rollNo, marks):
        print('Constructor execution...')
        self.name = name
        self.rollNo = rollNo
        self.marks = marks

    def printStudent(self):
        print('Method execution...')
        print('Hello {}'.format(self.name))
        print(self.rollNo)
        print(self.marks)


studentList = []
while True:
    studentList.append(Student(input('Enter Name:'), eval(input('Enter Roll No:')),
                               eval(input('Enter Marks:'))))
    print('Student Added')
    option = input('Press N/n to exit')
    if option.lower() == 'n':
        break

print('All Students')
for student in studentList:
    student.printStudent()
    print()

# Enter Name:Theja
# Enter Roll No:100
# Enter Marks:90
# Constructor execution...
# Student Added
# Press N/n to exitY
# Enter Name:KSRN
# Enter Roll No:1
# Enter Marks:100
# Constructor execution...
# Student Added
# Press N/n to exitN
# All Students
# Method execution...
# Hello Theja
# 100
# 90
#
# Method execution...
# Hello KSRN
# 1
# 100
