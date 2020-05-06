s = input('Enter a sub string:')
subs = input('Enter sub string:')
flag = False
pos = s.find(subs)
n = len(s)
count = 0
while pos != -1:
    count += 1
    print("Found at position", pos)
    pos = s.find(subs, pos + len(subs), n)
    if pos == -1:
        break
    flag = True
if flag == True:
    print(count, s.count(subs))
if flag == False:
    print("Not Found")

# Enter a sub string:abbababababacdefg
# Enter sub string:a
# Found at position 0
# Found at position 3
# Found at position 5
# Found at position 7
# Found at position 9
# Found at position 11
# 6 6

# Enter a sub string:abbababababacdefg
# Enter sub string:ab
# Found at position 0
# Found at position 3
# Found at position 5
# Found at position 7
# Found at position 9
# 5 5

# Enter a sub string:bbbbbbb
# Enter sub string:bbb
# Found at position 0
# Found at position 3
# 2 2

# Enter a sub string:abbababababacdefg
# Enter sub string:z
# Not Found
