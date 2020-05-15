class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print('Hi', self.name)
        print('Your Marks are:', self.marks)

    def grade(self):
        if self.marks >= 60:
            print('You got First Grade')
        elif self.marks >= 50:
            print('Yout got Second Grade')
        elif self.marks >= 35:
            print('You got Third Grade')
        else:
            print('You are Failed')


n = int(input('Enter number of students:'))
for i in range(n):
    name = input('Enter Name:')
    marks = int(input('Enter Marks:'))
    s = Student(name, marks)
    s.display()
    s.grade()
    print()

# Enter number of students:2
# Enter Name:ksrn
# Enter Marks:80
# Hi ksrn
# Your Marks are: 80
# You got First Grade
#
# Enter Name:theja
# Enter Marks:35
# Hi 35
# Your Marks are: 35
# You got Third Grade
