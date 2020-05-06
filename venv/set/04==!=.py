x = {"Dog", "Cat", "Rat"}
y = {"Dog", "Cat", "Rat"}
z = {"DOG", "CAT", "RAT"}
w = {"Cat", "Rat", "Dog"}

print('id(x) -> ', id(x))
print('id(y) -> ', id(y))
print('id(z) -> ', id(z))
print('id(w) -> ', id(w))

print(x == y)
print(x == z)
print(x == w)
print(x != z)
print(x != w)

# id(x) ->  140717723835528
# id(y) ->  140717754729416
# id(z) ->  140717723428232
# id(w) ->  140717723427784
# True
# False
# True
# True
# False
