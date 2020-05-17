class Professor:
    pass


class Department:
    def __init__(self, professor):
        self.professor = Professor()


professor = Professor()
itDepartment = Department(professor)
csDepartment = Department(professor)
