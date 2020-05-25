import os

cwd = os.getcwd()
print("Current Working Directory:", cwd)

os.mkdir('mysub')
# Run second time - Already exists
# Traceback (most recent call last):
#   File "/Code/venv/file/39Directory.py", line <>, in <module>
#     os.mkdir('mysub')
# FileExistsError: [Errno 17] File exists: 'mysub'

os.mkdir('mysub/mysub2')
# If mysub does not exist:
# Traceback (most recent call last):
#   File "/Code/venv/file/39Directory.py", line <>, in <module>
#     os.mkdir('mysub/mysub2')
# FileNotFoundError: [Errno 2] No such file or directory: 'mysub/mysub2'

os.mkdir('mysub1')
os.mkdir('mysub1/mysub2')
os.mkdir('mysub1/mysub2/mysub3')

# os.mkdir('/home/ksrntheja/mydir')

os.makedirs('sub1/sub2/sub3')
# Traceback (most recent call last):
#   File "/Code/venv/file/39Directory.py", line <>, in <module>
#     os.makedirs('sub1/sub2/sub3')
#   File "/usr/lib/python3.6/os.py", line 220, in makedirs
#     mkdir(name, mode)
# FileExistsError: [Errno 17] File exists: 'sub1/sub2/sub3'

os.rmdir('mysub/mysub2')
# os.rmdir('mysub')
# Traceback (most recent call last):
#   File "/Code/venv/file/39Directory.py", line <>, in <module>
#     os.rmdir('mysub')
# OSError: [Errno 39] Directory not empty: 'mysub'
# os.rmdir('mydbsub')
# Traceback (most recent call last):
#   File "/Code/venv/file/39Directory.py", line <>, in <module>
#     os.rmdir('mydbsub')
# FileNotFoundError: [Errno 2] No such file or directory: 'mydbsub'

os.removedirs('sub1/sub2/sub3')
# os.removedirs('sub1')
# Traceback (most recent call last):
#   File "/Code/venv/file/39Directory.py", line <>, in <module>
#     os.removedirs('sub1')
#   File "/usr/lib/python3.6/os.py", line 238, in removedirs
#     rmdir(name)
# OSError: [Errno 39] Directory not empty: 'sub1'
# os.removedirs('mydbsub')
#  Traceback (most recent call last):
#   File "/Code/venv/file/39Directory.py", line <>, in <module>
#     os.removedirs('mydbsub')
#   File "/usr/lib/python3.6/os.py", line 238, in removedirs
#     rmdir(name)
# FileNotFoundError: [Errno 2] No such file or directory: 'mydbsub'

os.mkdir('torename')
os.rename('torename', 'renamed')
# os.rename('torename', 'renamed')
# Traceback (most recent call last):
#   File "/Code/venv/file/39Directory.py", line <>, in <module>
#     os.rename('torename', 'renamed')
# FileNotFoundError: [Errno 2] No such file or directory: 'torename' -> 'renamed'
