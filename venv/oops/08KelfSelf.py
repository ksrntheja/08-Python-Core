class Student:

    def printStudent(kelf):
        print('Method execution...')
        print('Hello {}'.format(kelf.name))
        print(kelf.rollNo)
        print(kelf.marks)

    def __init__(self, name, rollNo, marks):
        print('Constructor execution...')
        self.name = name
        self.rollNo = rollNo
        self.marks = marks


s = Student('Thejaselfkelf', 100, 85)
print(s.name)
print(s.rollNo)
print(s.marks)
s.printStudent()

# Constructor execution...
# Thejaselfkelf
# 100
# 85
# Method execution...
# Hello Thejaselfkelf
# 100
# 85
