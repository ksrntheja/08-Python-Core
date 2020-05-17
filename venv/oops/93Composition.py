class University:
    def __init__(self):
        self.dept = self.Department()

    class Department:
        pass


university = University()
department = Department()

# Traceback (most recent call last):
#   File "/Code/venv/oops/93Composition.py", line <>, in <module>
#     department = Department()
# NameError: name 'Department' is not defined
