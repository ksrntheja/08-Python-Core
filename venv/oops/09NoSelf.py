class Student:

    def printStudent(kelf):
        print('Method execution...')
        print('Hello {}'.format(kelf.name))
        print(kelf.rollNo)
        print(kelf.marks)

    def __init__(name, rollNo, marks):
        print('Constructor execution...')
        self.name = name
        self.rollNo = rollNo
        self.marks = marks


s = Student('Thejaselfkelf', 100, 85)
print(s.name)
print(s.rollNo)
print(s.marks)
s.printStudent()

# Traceback (most recent call last):
#   File "/Code/venv/oops/09DefineCompleteClassNoSelf.py", line <>, in <module>
#     s = StudentComplete('Thejaselfkelf', 100, 85)
# TypeError: __init__() takes 3 positional arguments but 4 were given
