# Create List with elements present in l1 but not in l2:
l1 = [10, 20, 30, 40]
l2 = [30, 40, 50, 60]
# print(x for x in l1 if x not in l2)
# <generator object <genexpr> at 0x7f49b382e0a0>
print([x for x in l1 if x not in l2])

# Create List with elements present in both l1 and l2:
l1 = [10, 20, 30, 40]
l2 = [30, 40, 50, 60]
print([x for x in l1 if x in l2])

words = ["Balaiah", "Nag", "Venkatesh", "Chiranjeevi"]
l = [w[0] for w in words]
print(l)

print()

words = "the quick brown fox jumps over the lazy dog".split()
print(words)
l = [[word.upper(), len(word)] for word in words]
print(l)

# [10, 20]
# [30, 40]
# ['B', 'N', 'V', 'C']
#
# ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# [['THE', 3], ['QUICK', 5], ['BROWN', 5], ['FOX', 3], ['JUMPS', 5], ['OVER', 4], ['THE', 3], ['LAZY', 4], ['DOG', 3]]
