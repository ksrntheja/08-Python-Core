import json

json_string = '''{
                    "name": "theja",
                    "age": 35,
                    "salary": 1000.0,
                    "ismarried": true,
                    "ishavinggirlfriend": null
               }'''

# 'ishavinggirlfriend': null
# Traceback (most recent call last):
#   File "/Code/venv/serialization/05JsonToDict.py", line <>, in <module>
#     emp_dict = json.loads(json_string)
#   File "/usr/lib/python3.6/json/__init__.py", line 354, in loads
#     return _default_decoder.decode(s)
#   File "/usr/lib/python3.6/json/decoder.py", line 339, in decode
#     obj, end = self.raw_decode(s, idx=_w(s, 0).end())
#   File "/usr/lib/python3.6/json/decoder.py", line 355, in raw_decode
#     obj, end = self.scan_once(s, idx)
# json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes:
# line <> column <> (char 114)

emp_dict = json.loads(json_string)
print(emp_dict)
print('type(emp_dict)', type(emp_dict))

print()

print('Employee Name:', emp_dict['name'])
print('Employee Age:', emp_dict['age'])
print('Employee Salary:', emp_dict['salary'])
print('Is Employee Married:', emp_dict['ismarried'])
print('Is Employee Has GF:', emp_dict['ishavinggirlfriend'])

print()

for k, v in emp_dict.items():
    print('{} : {}'.format(k, v))

# {'name': 'theja', 'age': 35, 'salary': 1000.0, 'ismarried': True, 'ishavinggirlfriend': None}
# type(emp_dict) <class 'dict'>
#
# Employee Name: theja
# Employee Age: 35
# Employee Salary: 1000.0
# Is Employee Married: True
# Is Employee Has GF: None
#
# name : theja
# age : 35
# salary : 1000.0
# ismarried : True
# ishavinggirlfriend : None
