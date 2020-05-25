import json

employee = {'name': 'theja',
            'age': 35,
            'salary': 1000.0,
            "ismarried": True,
            'ishavinggirlfriend': None
            }
# print(employee)
# {'name': 'theja', 'age': 35, 'salary': 1000.0, 'ismarried': True, 'ishavinggirlfriend': None}
# json_string = json.dumps(employee)
# {"name": "theja", "age": 35, "salary": 1000.0, "ismarried": true, "ishavinggirlfriend": null}
# json_string = json.dumps(employee, indent=4)
# {
#     "name": "theja",
#     "age": 35,
#     "salary": 1000.0,
#     "ismarried": true,
#     "ishavinggirlfriend": null
# }
json_string = json.dumps(employee, indent=4, sort_keys=True)
print(json_string)
with open('emp.json', 'w') as f:
    json.dump(employee, f, indent=4)

# {
#     "age": 35,
#     "ishavinggirlfriend": null,
#     "ismarried": true,
#     "name": "theja",
#     "salary": 1000.0
# }


# emp.json
# {
#     "name": "theja",
#     "age": 35,
#     "salary": 1000.0,
#     "ismarried": true,
#     "ishavinggirlfriend": null
# }
