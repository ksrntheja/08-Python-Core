s = 'Learning Python is very very easy !!!'
l = list(s)
print(l)
print(type(l))

print()

l = list(s.split())
print(l)
print(type(l))

# ['L', 'e', 'a', 'r', 'n', 'i', 'n', 'g', ' ', 'P', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'v', 'e', 'r', 'y', ' ', 'v', 'e', 'r', 'y', ' ', 'e', 'a', 's', 'y', ' ', '!', '!', '!']
# <class 'list'>
#
# ['Learning', 'Python', 'is', 'very', 'very', 'easy', '!!!']
# <class 'list'>
