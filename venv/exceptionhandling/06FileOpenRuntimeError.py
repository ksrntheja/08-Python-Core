f = open('filenotfound.txt')
print(f.read())

# Traceback (most recent call last):
#   File "/Code/venv/exceptionhandling/06FileOpenRuntimeError.py", line <>, in <module>
#     f = open('filenotfound.txt')
# FileNotFoundError: [Errno 2] No such file or directory: 'filenotfound.txt'
