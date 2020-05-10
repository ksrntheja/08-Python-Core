def f01():
    global a = 10
    print(a)


def f02():
    print(a)


f01()
f02()

#   File "/Code/venv/functions/38GlobalKeywordDeclareAssignError", line <>
#     global a = 10
#              ^
# SyntaxError: invalid syntax
