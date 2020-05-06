s = "abab"
print(s, "is available at :", id(s))
s = s.replace("a", "b")
print(s, "is available at :", id(s))

# abab is available at : 140697379107704
# bbbb is available at : 140697379107872
