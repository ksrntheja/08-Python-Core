def wish01(name, msg):
    print("Hello", name, msg)


def wish02(name='Guest', msg='Good Morning'):
    print("Hello", name, msg)


def wish03(name, msg='Good Morning'):
    print("Hello", name, msg)


# def wish04(name='Guest', msg):
#     print("Hello", name, msg)


#   File "/Code/venv/functions/20DefaultArgv.py", line <>
#     def wish04(name='Guest', msg):
#               ^
# SyntaxError: non-default argument follows default argument


wish01("Theja", "Good Morning")
wish02()
wish03("Theja")

# Hello Theja Good Morning
# Hello Guest Good Morning
# Hello Theja Good Morning
