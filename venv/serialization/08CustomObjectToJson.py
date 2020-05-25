import json


class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print('ENO:{}, ENAME:{}, ESAL:{}, EADDR:{}'.format(self.eno, self.ename, self.esal, self.eaddr))

    def __str__(self):
        return 'ENO:{}, ENAME:{}, ESAL:{}, EADDR:{}'.format(self.eno, self.ename, self.esal, self.eaddr)


e = Employee(100, 'Theja', 1000, 'Hyderabad')

# print(e)
# <__main__.Employee object at 0x7fd10bdae588>
# If __str__(self) is there:
# ENO:100, ENAME:Theja, ESAL:1000, EADDR:Hyderabad

# json_string = json.dumps(e)
# Traceback (most recent call last):
#   File "/Code/venv/serialization/08CustomObjectToJson.py", line <>, in <module>
#     json_string = json.dumps(e)
#   File "/usr/lib/python3.6/json/__init__.py", line 231, in dumps
#     return _default_encoder.encode(obj)
#   File "/usr/lib/python3.6/json/encoder.py", line 199, in encode
#     chunks = self.iterencode(o, _one_shot=True)
#   File "/usr/lib/python3.6/json/encoder.py", line 257, in iterencode
#     return _iterencode(o, 0)
#   File "/usr/lib/python3.6/json/encoder.py", line 180, in default
#     o.__class__.__name__)
# TypeError: Object of type 'Employee' is not JSON serializable

emp_dict = {'eno': e.eno, 'ename': e.ename, 'esal': e.esal, 'eaddr': e.eaddr}
print(emp_dict)
e_dict = e.__dict__
print(e_dict)
print(emp_dict == e_dict)

json_string = json.dumps(e_dict, indent=4)
print(json_string)

with open('emp.json', 'w') as f:
    json.dump(e_dict, f, indent=4)

with open('emp.json', 'r') as f:
    e_dict = json.load(f)
    print('type(e_dict)', type(e_dict))
    print(e_dict)

# {'eno': 100, 'ename': 'Theja', 'esal': 1000, 'eaddr': 'Hyderabad'}
# {'eno': 100, 'ename': 'Theja', 'esal': 1000, 'eaddr': 'Hyderabad'}
# True
# {
#     "eno": 100,
#     "ename": "Theja",
#     "esal": 1000,
#     "eaddr": "Hyderabad"
# }
# type(e_dict) <class 'dict'>
# {'eno': 100, 'ename': 'Theja', 'esal': 1000, 'eaddr': 'Hyderabad'}
