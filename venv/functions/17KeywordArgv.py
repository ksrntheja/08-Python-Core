def wish(name, msg):
    print("Hello", name, msg)


wish("Theja", "GoodMorning")
wish("Theja", msg="GoodMorning")

# wish(name="Theja", "GoodMorning")

#   File "/Code/venv/functions/17KeywordArgv.py", line <>
#     wish(name="Theja", "GoodMorning")
#                       ^
# SyntaxError: positional argument follows keyword argument

# Hello Theja GoodMorning
# Hello Theja GoodMorning
