class StudentComplete:

    def printStudent(self):
        print('Method execution...')
        print('Hello {}'.format(self.name))
        print(self.rollNo)
        print(self.marks)

    def __init__(self, name, rollNo, marks):
        print('Constructor execution...')
        self.name = name
        self.rollNo = rollNo
        self.marks = marks


s = StudentComplete('Theja', 100, 85)
print(s.name)
print(s.rollNo)
print(s.marks)
s.printStudent()  # No need to pass 'self' argument. Internally PVM will take care

# Constructor execution...
# Theja
# 100
# 85
# Method execution...
# Hello Theja
# 100
# 85
