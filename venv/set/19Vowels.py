w = input("Enter word to search for vowels: ")
s = set(w)
v = {'a', 'e', 'i', 'o', 'u'}
d = s.intersection(v)
print("The different vowel present in", w, "are", d)

# Enter word to search for vowels: Apple
# The different vowel present in Apple are {'e'}
