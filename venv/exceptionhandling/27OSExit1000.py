import os

try:
    print("try")
    os._exit(1000)
except ValueError:
    print("except")
finally:
    print("finally")

# try
