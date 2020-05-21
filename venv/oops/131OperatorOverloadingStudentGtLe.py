class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __le__(self, other):
        return self.marks <= other.marks


print('10 > 20 :', 10 > 20)
print('10 < 20 :', 10 < 20)
student01 = Student('ksrn', 100)
student02 = Student('theja', 200)
print('student01 > student02 :', student01 > student02)
print('student01 < student02 :', student01 < student02)
print('student01 <= student02 :', student01 <= student02)
print('student01 >= student02 :', student01 >= student02)

# 10 > 20 : False
# 10 < 20 : True
# student01 > student02 : False
# student01 < student02 : True
# student01 <= student02 : True
# student01 >= student02 : False
