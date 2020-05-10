def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False


l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(isEven(), l)))

# Traceback (most recent call last):
#   File "/Code/venv/functions/56WithFilterEvenNumbers.py", line <>, in <module>
#     print(list(filter(isEven(), l)))
# TypeError: isEven() missing 1 required positional argument: 'x'
