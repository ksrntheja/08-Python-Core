s = input("Enter main string:")
subs = input("Enter sub string:")
print(s.index(subs))

# Enter main string:learning python is very easy
# Enter sub string:Python
# Traceback (most recent call last):
#   File "/Code/venv/strings/String022Index.py", line <>, in <module>
#     print(s.index(subs))
# ValueError: substring not found

# Enter main string:learning python is very easy
# Enter sub string:<space>
# 8

# Enter main string:learning python is very easy
# Enter sub string:<enter>
# 0
