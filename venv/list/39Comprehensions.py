vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Enter the word to search for vowels: ")

# l = []

# unique = []
# l = [unique.append(char) for char in word if char in vowels and char not in unique]
# print(unique)
# ['e', 'u', 'i', 'o', 'a']

# l = [char for char in word if (char in vowels) and (char not in l)]
# print(l)
# [None, None, None, None, None]

print([char for char in vowels if char in word])

# Enter the word to search for vowels: the quick brown fox jumps over the lazy dog
# ['a', 'e', 'i', 'o', 'u']
