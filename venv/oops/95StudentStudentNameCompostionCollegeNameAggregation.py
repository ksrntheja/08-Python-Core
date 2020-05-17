class Student:
    collegeName = 'ThejaCollege'

    def __init__(self, name):
        self.name = name
        print(Student.collegeName)


s = Student('Theja')
print(s.name)

# ThejaCollege
# Theja
