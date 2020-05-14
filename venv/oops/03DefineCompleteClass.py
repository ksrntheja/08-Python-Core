class StudentComplete:
    """Demo student doc"""

    def __init__(self):
        print('Constructor execution...')
        self.name = 'Theja'
        self.rollNo = 100
        self.marks = 85

    def printStudent(self):
        print('Method execution...')
        print('Hello {}'.format(self.name))
        print(self.rollNo)
        print(self.marks)


s = StudentComplete()
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
