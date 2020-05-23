f = None
try:
    f = open('34TryExceptElseFinally02.py', 'r')
except:
    print('No file present')
else:
    print('file opened -> ')
    print(f.read())
finally:
    if f is not None:
        f.close()

# file opened ->
# try:
#     print('try')
#     print(10 / 0)
# except:
#     print('except')
# else:
#     print('else')
# finally:
#     print('finally')
#
# # try
# # except
# # finally

# No file present
