import jsonpickle

# pip3 install jsonpickle
print(jsonpickle)


class Employee:
    def __init__(self, eno, ename, esal, eaddr, isMarried):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr
        self.isMarried = isMarried

    def display(self):
        print('ENO:{}, ENAME:{}, ESAL:{}, EADDR:{}, ISMARRIED:{}'
              .format(self.eno, self.ename, self.esal, self.eaddr, self.isMarried))

    def __str__(self):
        return 'ENO:{}, ENAME:{}, ESAL:{}, EADDR:{}, ISMARRIED:{}' \
            .format(self.eno, self.ename, self.esal, self.eaddr, self.isMarried)


e = Employee(100, 'Theja', 1000, 'Hyderabad', True)
# emp_dict = {'eno': e.eno, 'ename': e.ename, 'esal': e.esal, 'eaddr': e.eaddr, 'isMarried': e.isMarried}
# e_dict = e.__dict__
# print(emp_dict == e_dict)

json_string = jsonpickle.encode(e, indent=4)
print(json_string)
with open('emp.json', 'w') as f:
    f.write(json_string)

e = jsonpickle.decode(json_string)
print('type(e)', type(e))
e.display()
with open('emp.json', 'r') as f:
    e_string = f.read()
    e = jsonpickle.decode(e_string)
    e.display()

# <module 'jsonpickle' from '/home/ksrntheja/.local/lib/python3.6/site-packages/jsonpickle/__init__.py'>
# {
#     "py/object": "__main__.Employee",
#     "eno": 100,
#     "ename": "Theja",
#     "esal": 1000,
#     "eaddr": "Hyderabad",
#     "isMarried": true
# }
# type(e) <class '__main__.Employee'>
# ENO:100, ENAME:Theja, ESAL:1000, EADDR:Hyderabad, ISMARRIED:True
# ENO:100, ENAME:Theja, ESAL:1000, EADDR:Hyderabad, ISMARRIED:True

# emp.json
# {
#     "py/object": "__main__.Employee",
#     "eno": 100,
#     "ename": "Theja",
#     "esal": 1000,
#     "eaddr": "Hyderabad",
#     "isMarried": true
# }
