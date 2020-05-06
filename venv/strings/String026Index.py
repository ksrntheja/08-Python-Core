s = 'learning python is very easy'
try:
    print("s.index('y', 23, 30) -> ", s.index('y', 23, 30))
    print("s.index('y', 22, 30) -> ", s.index('y', 22, 30))
    # print("s.index('y', 23, 27) -> ", s.index('y', 23, 27))
    print("s.index('y', 22, 27) -> ", s.index('y', 22, 27))
    # print("s.index('y', -6, 22) -> ", s.index('y', -6, 22))
    # print("s.index('y', 22, -6) -> ", s.index('y', 22, -6))
    print("s.index('y', -6, 23) -> ", s.index('y', -6, 23))
    # print("s.index('y', 23, -6) -> ", s.index('y', 23, -6))
    # print("s.index('e', -1, 23) -> ", s.index('e', -1, 23))
    print("s.index('e', 23, -1) -> ", s.index('e', 23, -1))
    # print("s.index('e', -1, -5) -> ", s.index('e', -1, -5))
    print("s.index('e', -5, -1) -> ", s.index('e', -5, -1))
except ValueError:
    print("substring not found")
else:
    print("substring found")

# s.index('y', 23, 30) ->  27
# s.index('y', 22, 30) ->  22
# s.index('y', 22, 27) ->  22
# s.index('y', -6, 23) ->  22
# s.index('e', 23, -1) ->  24
# s.index('e', -5, -1) ->  24
# substring found
