s = "Learning Python is very difficult"
print(s)
s1 = s.replace("difficult", "easy")
print(s1)

s = "ababababababab"
print(s)
s1 = s.replace("a", "b")
print(s1)

s = "hello world !"
print(s)
s1 = s.replace(" ", "")
print(s1)
print("No of spaces is", len(s) - len(s1))

s = "Learning Python is very Difficult"
print(s)
s1 = s.replace("difficult", "Easy")
print(s1)

# Learning Python is very difficult
# Learning Python is very easy
# ababababababab
# bbbbbbbbbbbbbb
# hello world !
# helloworld!
# No of spaces is 2
# Learning Python is very Difficult
# Learning Python is very Difficult
