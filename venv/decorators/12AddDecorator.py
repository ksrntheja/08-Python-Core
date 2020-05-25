def decor_for_add(func):
    # def inner(x, y, z):
    # Traceback (most recent call last):
    #   File "/Code/venv/decorators/12AddDecorator.py", line <>, in <module>
    #     add(10, 20)
    # TypeError: inner() missing 1 required positional argument: 'z'
    # def inner(x):
    # Traceback (most recent call last):
    #   File "/Code/venv/decorators/12AddDecorator.py", line <>, in <module>
    #     add(10, 20)
    # TypeError: inner() takes 1 positional argument but 2 were given
    def inner(x, y, z):
        print('#' * 30)
        print('The sum = ', end='')
        func(x, y)  # Function Aliasing
        print('#' * 30)

    return inner


@decor_for_add
def add(a, b):
    print(a + b)


add(10, 20)

# ##############################
# The sum = 30
# ##############################
