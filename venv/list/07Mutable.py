n = [10, 20, 30, 40]
print('n ->', n, 'id(n) -> ', id(n))
print('n[1] ->', n[1], 'id(n[1]) -> ', id(n[1]))
n[1] = 777
print('n[1] ->', n[1], 'id(n[1]) -> ', id(n[1]))
print('n ->', n, 'id(n) -> ', id(n))

print('id(20)  ->', id(20))
print('id(777) ->', id(777))

# n -> [10, 20, 30, 40] id(n) ->  140528798591112
# n[1] -> 20 id(n[1]) ->  10915104
# n[1] -> 777 id(n[1]) ->  140528799256016
# n -> [10, 777, 30, 40] id(n) ->  140528798591112
# id(20)  -> 10915104
# id(777) -> 140528799256016
