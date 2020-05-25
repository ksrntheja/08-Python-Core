@decor_for_add
def add(a, b):
    print(a + b)


def decor_for_add(func):
    def inner(x, y, z):
        print('#' * 30)
        print('The sum = ', end='')
        func(x, y)  # Function Aliasing
        print('#' * 30)

    return inner


add(10, 20)

# Traceback (most recent call last):
#   File "/Code/venv/decorators/13DecoratorOrder.py", line <>, in <module>
#     @decor_for_add
# NameError: name 'decor_for_add' is not defined