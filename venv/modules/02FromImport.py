from Test import x, add

print('t.x :', x)
# print('t.y :', y)
# Traceback (most recent call last):
#   File "/Code/venv/modules/02FromImport.py", line <>, in <module>
#     print('t.y :', y)
# NameError: name 'y' is not defined

add(10, 20)
# product(10, 20)
# Traceback (most recent call last):
#   File "/Code/venv/modules/02FromImport.py", line <>, in <module>
#     product(10, 20)
# NameError: name 'product' is not defined

# Test.product(10, 20)
# Traceback (most recent call last):
#   File "/Code/venv/modules/02FromImport.py", line <>, in <module>
#     Test.product(10, 20)
# NameError: name 'Test' is not defined

# t.x : 10
# The sum : 30
