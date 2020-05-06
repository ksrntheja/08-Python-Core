s = "abab"
s1 = s.replace("a", "b")
print(s, "is available at :", id(s))
print(s1, "is available at :", id(s1))

# abab is available at : 139660445664120
# bbbb is available at : 139660445664288
