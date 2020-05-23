try:
    print("try")
    print(10 / 0)
except ValueError:
    print("except")
finally:
    print("finally")

# try
# finally
# Traceback (most recent call last):
#   File "/Code/venv/exceptionhandling/25TryExceptFinally03.py", line <>, in <module>
#     print(10 / 0)
# ZeroDivisionError: division by zero
