def squareIt(x):
    return x ** x


try:
    assert squareIt(2) == 4, "The square of 2 should be 4"
    assert squareIt(3) == 9, "The square of 3 should be 9"
    assert squareIt(4) == 16, "The square of 4 should be 16"
    print(squareIt(2))
    print(squareIt(3))
    print(squareIt(4))
except:
    print('In Except')
print('Hi')

# In Except
# Hi
