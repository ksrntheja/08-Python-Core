import datetime

today = datetime.datetime.now()
s = str(today)  # converting datetime object to str
print(s)
d = eval(s)  # converting str object to datetime

# 2020-05-21 20:45:11.786408
# Traceback (most recent call last):
#   File "/Code/venv/oops/189str.py", line <>, in <module>
#     d = eval(s)  # converting str object to datetime
#   File "<string>", line 1
#     2020-05-21 20:45:11.786408
#           ^
# SyntaxError: invalid token
