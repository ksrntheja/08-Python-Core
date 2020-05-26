s = input('Enter a String to reverse:')

listOfWords = s.split()
print(listOfWords)
listOfWords = list(map(lambda s: s[::-1], listOfWords))
print(' '.join(listOfWords))

# Enter a String to reverse:Learning Python Is Very Easy
# ['Learning', 'Python', 'Is', 'Very', 'Easy']
# gninraeL nohtyP sI yreV ysaE
