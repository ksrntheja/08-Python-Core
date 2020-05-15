class Person:
    def __init__(self, name, dd, mm, yyyy):
        print('Person Object Creation...')
        self.name = name
        self.dob = self.Dob(dd, mm, yyyy)

    def display(self):
        print('Name:', self.name)
        print('Calling DOB Display')
        self.dob.display()

    class Dob:
        def __init__(self, dd, mm, yyyy):
            print('Dob Object Creation...')
            self.dd = dd
            self.mm = mm
            self.yy = yyyy

        def display(self):
            print('Dob={}/{}/{}'.format(self.dd, self.mm, self.yy))


p = Person('Theja', 15, 8, 1947)
p.display()

# Person Object Creation...
# Dob Object Creation...
# Name: Theja
# Calling DOB Display
# Dob=15/8/1947