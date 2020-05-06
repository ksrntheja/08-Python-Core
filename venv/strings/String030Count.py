s = 'learning python is very easy'
print("s.count('y')          ->", s.count('y'))
print("s.count('y', 22, 30)  ->", s.count('y', 22, 30))
print("s.count('y', 23, 30)  ->", s.count('y', 23, 30))
print("s.count('y', -1, -5)  ->", s.count('y', -1, -5))
print("s.count('y', -5, -1)  ->", s.count('y', -5, -1))
print("s.count('y', -5, 0)   ->", s.count('y', -5, 0))
print("s.count('y', -28, -1) ->", s.count('y', -28, -1))

print("s.count('e', -5, -1)  ->", s.count('e', -5, -1))
print("s.count('e', -1, -5)  ->", s.count('e', -1, -5))

# s.count('y')          -> 3
# s.count('y', 22, 30)  -> 2
# s.count('y', 23, 30)  -> 1
# s.count('y', -1, -5)  -> 0
# s.count('y', -5, -1)  -> 0
# s.count('y', -5, 0)   -> 0
# s.count('y', -28, -1) -> 2
# s.count('e', -5, -1)  -> 1
# s.count('e', -1, -5)  -> 0
