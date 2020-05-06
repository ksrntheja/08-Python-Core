s = input("Enter mail id:")
try:
    i = s.index('@')
    print("mail id valid", i)
except ValueError:
    print("mail id not valid")

# Enter mail id:theja@gmail.com
# mail id valid 5

# Enter mail id:theja$gmail.com
# mail id not valid
