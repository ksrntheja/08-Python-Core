x = ["Dog", "Cat", "Rat"]
y = ["Dog", "Cat", "Rat"]
z = ["DOG", "CAT", "RAT"]
w = ["Cat", "Rat", "Dog"]

print('id(x) -> ', id(x))
print('id(y) -> ', id(y))
print('id(z) -> ', id(z))
print('id(w) -> ', id(w))

print(x == y)
print(x == z)
print(x == w)
print(x != z)
print(x != w)

# id(x) ->  140382461466760
# id(y) ->  140382461466696
# id(z) ->  140382461466568
# id(w) ->  140382461466504
# True
# False
# False
# True
# True
