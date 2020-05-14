class Student:
    schoolName = 'A school'  # STATIC variable

    def __init__(self, name, rollNo, marks):
        self.name = name  # INSTANCE variable
        self.rollNo = rollNo  # INSTANCE variable
        self.marks = marks  # INSTANCE variable

    def printStudent(self):
        x = 10  # LOCAL variable
        for i in range(x):  # i is LOCAL variable
            print('*', end='')
        print()
        print('Hello {}'.format(self.name))
        print(self.rollNo)
        print(self.marks)
        print(self.schoolName)
        # print(schoolName)
        # NameError: name 'schoolName' is not defined


s = Student('Theja', 100, 85)
print('s.name   -> ', s.name)
print('s.rollNo -> ', s.rollNo)
print('s.marks  -> ', s.marks)
print('s.schoolName       -> ', s.schoolName)
print('Student.schoolName -> ', Student.schoolName)
s.printStudent()

# s.name   ->  Theja
# s.rollNo ->  100
# s.marks  ->  85
# s.schoolName       ->  A school
# Student.schoolName ->  A school
# **********
# Hello Theja
# 100
# 85
# A school
