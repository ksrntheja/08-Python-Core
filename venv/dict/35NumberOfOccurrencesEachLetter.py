word = input("Enter dictionary:")
d = {}
for letter in word:
    d[letter] = d.get(letter, 0) + 1
for k, v in d.items():
    print(k, '->', v)

# Enter dictionary:mississippi
# m -> 1
# i -> 4
# s -> 4
# p -> 2
