import os

try:
    print("try")
    os._exit(0)
except ValueError:
    print("except")
finally:
    print("finally")

# try
