a = 10


def f01():
    print(a)
    global a
    a = 20
    print(a)


f01()

#   File "/Code/venv/functions/39GlobalKeywordPrior.py", line <>
#     global a
#     ^
# SyntaxError: name 'a' is used prior to global declaration
