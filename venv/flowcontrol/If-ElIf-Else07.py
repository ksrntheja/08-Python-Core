words = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
n = int(input("Enter a digit from 0 to 9:"))
if n < 10:
    print(words[n])
else:
    print("PLEASE ENTER A DIGIT FROM 0 TO 9")

# Enter a digit from 0 to 9:0
# ZERO
# Enter a digit from 0 to 9:8
# EIGHT
# Enter a digit from 0 to 9:100
# PLEASE ENTER A DIGIT FROM 0 TO 9
