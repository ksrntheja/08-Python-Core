s = input('Enter a String to reverse:')

listOfWords = s.split()
print(listOfWords)
listOfWords = listOfWords[::-1]
print(' '.join(listOfWords))

# Enter a String to reverse:Learning Python Is Very Easy
# ['Learning', 'Python', 'Is', 'Very', 'Easy']
# Easy Very Is Python Learning
