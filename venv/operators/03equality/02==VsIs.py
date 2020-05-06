l1 = [10, 20, 30]
l2 = [10, 20, 30]
print('l1 is l2 -> ', l1 is l2)
print('l1 == l2 -> ', l1 == l2)
print('id(l1) -> ', id(l1))
print('id(l1) -> ', id(l2))
l3 = l1
print('l1 is l3 -> ', l1 is l3)
print('l2 is l3 -> ', l2 is l3)

# l1 is l2 ->  False
# l1 == l2 ->  True
# id(l1) ->  140377928386760
# id(l1) ->  140377928386696
# l1 is l3 ->  True
# l2 is l3 ->  False
