class A(B):
    pass


class B(A):
    pass

# Traceback (most recent call last):
#   File "/Code/venv/oops/107CyclicTwoClass.py", line <>, in <module>
#     class A(B):
# NameError: name 'B' is not defined
