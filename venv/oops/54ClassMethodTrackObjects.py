class Student:
    count = 0

    def __init__(self):
        Student.count += 1

    @classmethod
    def getNoOfObjects(cls):
        print('No of Objects:', cls.count)


Student.getNoOfObjects()
s1 = Student()
s2 = Student()
s3 = Student()
Student.getNoOfObjects()

# No of Objects: 0
# No of Objects: 3
