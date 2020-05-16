class Test:
    def __init__(self):
        print("Constructor")

    def __del__(self):
        print("Destructor")


t = Test()
print('"t" created')
print('del "t"')
del t
print('Accessing "t"')
print(t)
print("End of application")

# Constructor
# "t" created
# del "t"
# Destructor
# Accessing "t"
# Traceback (most recent call last):
#   File "/Code/venv/oops/79DelT.py", line <>, in <module>
#     print(t)
# NameError: name 't' is not defined
