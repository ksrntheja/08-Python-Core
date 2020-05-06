s1 = 'Python'
s2 = s1
s3 = s2
print(id(s1), id(s2), id(s3))
print(s1, s2, s3)
del s1
print(id(s2), id(s3))
print(s2, s3)
del s2, s3
print(s2, s3)

# 139906139629752 139906139629752 139906139629752
# Python Python Python
# 139906139629752 139906139629752
# Python Python
# Traceback (most recent call last):
#   File "/Code/venv/flowcontrol/Del02.py", line 10, in <module>
#     print(s2, s3)
# NameError: name 's2' is not defined
