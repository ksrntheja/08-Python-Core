from Test import *

print('t.x :', x)
print('t.y :', y)

add(10, 20)
product(10, 20)

Test.product(10, 20)

# t.x : 10
# t.y : 20
# The sum : 30
# The product : 200
# Traceback (most recent call last):
#   File "/Code/venv/modules/03FromImportStar.py", line <>, in <module>
#     Test.product(10, 20)
# NameError: name 'Test' is not defined
