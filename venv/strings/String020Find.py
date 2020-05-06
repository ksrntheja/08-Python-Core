s = "learning python is very easy"
print(s.find("python"))
print(s.find("Java"))
print(s.find("r"))
print(s.rfind("r"))

print("s.find('y', 23, 30) -> ", s.find('y', 23, 30))
print("s.find('y', 22, 30) -> ", s.find('y', 22, 30))
print("s.find('y', 23, 27) -> ", s.find('y', 23, 27))
print("s.find('y', 22, 27) -> ", s.find('y', 22, 27))
print("s.find('y', -6, 22) -> ", s.find('y', -6, 22))
print("s.find('y', 22, -6) -> ", s.find('y', 22, -6))
print("s.find('y', -6, 23) -> ", s.find('y', -6, 23))
print("s.find('y', 23, -6) -> ", s.find('y', 23, -6))
print("s.find('e', -1, 23) -> ", s.find('e', -1, 23))
print("s.find('e', 23, -1) -> ", s.find('e', 23, -1))
print("s.find('e', -1, -5) -> ", s.find('e', -1, -5))
print("s.find('e', -5, -1) -> ", s.find('e', -5, -1))

print()

print("s.rfind('y', 23, 30) -> ", s.rfind('y', 23, 30))
print("s.rfind('y', 22, 30) -> ", s.rfind('y', 22, 30))
print("s.rfind('y', 23, 27) -> ", s.rfind('y', 23, 27))
print("s.rfind('y', 22, 27) -> ", s.rfind('y', 22, 27))
print("s.rfind('y', -6, 22) -> ", s.rfind('y', -6, 22))
print("s.rfind('y', 22, -6) -> ", s.rfind('y', 22, -6))
print("s.rfind('y', -6, 23) -> ", s.rfind('y', -6, 23))
print("s.rfind('y', 23, -6) -> ", s.rfind('y', 23, -6))
print("s.rfind('e', -1, 23) -> ", s.rfind('e', -1, 23))
print("s.rfind('e', 23, -1) -> ", s.rfind('e', 23, -1))
print("s.rfind('e', -1, -5) -> ", s.rfind('e', -1, -5))
print("s.rfind('e', -5, -1) -> ", s.rfind('e', -5, -1))

print()

print("s[-1: 23]    -> ", s[-1: 23])
print("s[-1: 23:-1] -> ", s[-1: 23:-1])

# 9
# -1
# 3
# 21
# s.find('y', 23, 30) ->  27
# s.find('y', 22, 30) ->  22
# s.find('y', 23, 27) ->  -1
# s.find('y', 22, 27) ->  22
# s.find('y', -6, 22) ->  -1
# s.find('y', 22, -6) ->  -1
# s.find('y', -6, 23) ->  22
# s.find('y', 23, -6) ->  -1
# s.find('e', -1, 23) ->  -1
# s.find('e', 23, -1) ->  24
# s.find('e', -1, -5) ->  -1
# s.find('e', -5, -1) ->  24
#
# s.rfind('y', 23, 30) ->  27
# s.rfind('y', 22, 30) ->  27
# s.rfind('y', 23, 27) ->  -1
# s.rfind('y', 22, 27) ->  22
# s.rfind('y', -6, 22) ->  -1
# s.rfind('y', 22, -6) ->  -1
# s.rfind('y', -6, 23) ->  22
# s.rfind('y', 23, -6) ->  -1
# s.rfind('e', -1, 23) ->  -1
# s.rfind('e', 23, -1) ->  24
# s.rfind('e', -1, -5) ->  -1
# s.rfind('e', -5, -1) ->  24
#
# s[-1: 23]    ->
# s[-1: 23:-1] ->  ysae
