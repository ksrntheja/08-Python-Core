import json

with open('emp.json', 'r') as f:
    emp_dict = json.load(f)
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
