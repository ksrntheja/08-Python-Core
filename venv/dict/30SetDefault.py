d = {100: "theja", 200: "ravi", 300: "shiva"}
print(d.setdefault(400, "pavan"))
print(d)
print(d.setdefault(100, "sachin"))
print(d)

# pavan
# {100: 'theja', 200: 'ravi', 300: 'shiva', 400: 'pavan'}
# theja
# {100: 'theja', 200: 'ravi', 300: 'shiva', 400: 'pavan'}
