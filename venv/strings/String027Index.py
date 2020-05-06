s = 'learning python is very easy'
try:
    print("s.rindex('y', 23, 30) -> ", s.rindex('y', 23, 30))
    print("s.rindex('y', 22, 30) -> ", s.rindex('y', 22, 30))
    # print("s.rindex('y', 23, 27) -> ", s.rindex('y', 23, 27))
    print("s.rindex('y', 22, 27) -> ", s.rindex('y', 22, 27))
    # print("s.rindex('y', -6, 22) -> ", s.rindex('y', -6, 22))
    # print("s.rindex('y', 22, -6) -> ", s.rindex('y', 22, -6))
    print("s.rindex('y', -6, 23) -> ", s.rindex('y', -6, 23))
    # print("s.rindex('y', 23, -6) -> ", s.rindex('y', 23, -6))
    # print("s.rindex('e', -1, 23) -> ", s.rindex('e', -1, 23))
    print("s.rindex('e', 23, -1) -> ", s.rindex('e', 23, -1))
    # print("s.rindex('e', -1, -5) -> ", s.rindex('e', -1, -5))
    print("s.rindex('e', -5, -1) -> ", s.rindex('e', -5, -1))
except ValueError:
    print("substring not found")
else:
    print("substring found")

# s.rindex('y', 23, 30) ->  27
# s.rindex('y', 22, 30) ->  27
# s.rindex('y', 22, 27) ->  22
# s.rindex('y', -6, 23) ->  22
# s.rindex('e', 23, -1) ->  24
# s.rindex('e', -5, -1) ->  24
# substring found
