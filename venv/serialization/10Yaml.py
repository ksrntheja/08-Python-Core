from pyaml import yaml

emp_dict = {'name': 'Theja', 'age': 35, 'salary': 1000.0, 'isMarried': True}

yaml_string = yaml.dump(emp_dict)
print(yaml_string)

with open('emp.yaml', 'w') as f:
    yaml.dump(emp_dict, f)

# ed = yaml.load(yaml_string)
# /Code/venv/serialization/10Yaml.py:<>: YAMLLoadWarning: calling yaml.load() without Loader=... is deprecated, as the default Loader is unsafe. Please read https://msg.pyyaml.org/load for full details.
#   ed = yaml.load(yaml_string)

ed = yaml.safe_load(yaml_string)
# print('type(ed)', type(ed))
print(ed)

for k, v in ed.items():
    print(k, ':', v)

with open('emp.yaml', 'r') as f:
    edf = yaml.safe_load(f)
print(edf)

# age: 35
# isMarried: true
# name: Theja
# salary: 1000.0
#
# type(ed) <class 'dict'>
# {'age': 35, 'isMarried': True, 'name': 'Theja', 'salary': 1000.0}
# age : 35
# isMarried : True
# name : Theja
# salary : 1000.0
# {'age': 35, 'isMarried': True, 'name': 'Theja', 'salary': 1000.0}

# emp.yml
# age: 35
# isMarried: true
# name: Theja
# salary: 1000.0
#
