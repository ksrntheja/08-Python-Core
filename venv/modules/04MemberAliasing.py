from Test import add as a, product as p

a(10, 20)
p(10, 20)

Test.product(10, 20)

# The sum : 30
# The product : 200
# Traceback (most recent call last):
#   File "/Code/venv/modules/04MemberAliasing.py", line <>, in <module>
#     Test.product(10, 20)
# NameError: name 'Test' is not defined
