class Student:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks


n = int(input('Enter number of students:'))
for i in range(n):
    s = Student()
    name = input('Enter Name:')
    s.setName(name)
    marks = int(input('Enter Marks:'))
    s.setMarks(marks)
    print('Hi', s.getName())
    print('Your Marks are:', s.getMarks())
    print()

# Enter number of students:2
# Enter Name:ksrn
# Enter Marks:80
# Hi ksrn
# Your Marks are: 80
#
# Enter Name:theja
# Enter Marks:35
# Hi theja
# Your Marks are: 35
