word = input("Enter any word: ")
vowels = {'a', 'e', 'i', 'o', 'u'}
d = {}
for x in word:
    if x in vowels:
        d[x] = d.get(x, 0) + 1
for k, v in d.items():
    print(k, "occurred ", v, " times")

# Enter any word: doganimaldoganimal
# o occurred  2  times
# a occurred  4  times
# i occurred  2  times
