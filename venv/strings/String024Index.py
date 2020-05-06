s = input("Enter main string:")
subs = input("Enter sub string:")
try:
    n = s.rindex(subs)
    print(n)
except ValueError:
    print("substring not found")
else:
    print("substring found")

# Enter main string:learning python is very easy
# Enter sub string:y
# 27
# substring found

# Enter main string:learning python is very easy
# Enter sub string:yy
# substring not found

# Enter main string:learning python is very easy
# Enter sub string:<space>
# 23
# substring found

# Enter main string:learning python is very easy
# Enter sub string:<enter>
# 28
# substring found
