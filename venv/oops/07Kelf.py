class Student:

    def printStudent(kelf):
        print('Method execution...')
        print('Hello {}'.format(kelf.name))
        print(kelf.rollNo)
        print(kelf.marks)

    def __init__(kelf, name, rollNo, marks):
        print('Constructor execution...')
        kelf.name = name
        kelf.rollNo = rollNo
        kelf.marks = marks


s = Student('Thejakelf', 100, 85)
print(s.name)
print(s.rollNo)
print(s.marks)
s.printStudent()

# Constructor execution...
# Thejakelf
# 100
# 85
# Method execution...
# Hello Thejakelf
# 100
# 85
