s = input("Enter main string:")
subs = input("Enter sub string:")
try:
    n = s.index(subs)
    print(n)
except ValueError:
    print("substring not found")
else:
    print("substring found")

# Enter main string:learning python is very easy
# Enter sub string:python
# 9
# substring found

# Enter main string:learning python is very easy
# Enter sub string:Python
# substring not found

# Enter main string:learning python is very easy
# Enter sub string:<enter>
# 0
# substring found

# Enter main string:learning python is very easy
# Enter sub string:
# 8
# substring found
