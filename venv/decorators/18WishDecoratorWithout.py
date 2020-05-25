def decor(func):
    def inner(name):
        if name == "ksrn":
            print("Hello ksrn Bad Morning")
        else:
            func(name)

    return inner


def wish(name):
    print("Hello", name, "Good Morning")


decorfunction = decor(wish)

wish("theja")
wish("ksrn")

print()

decorfunction("theja")
decorfunction("ksrn")

# Hello theja Good Morning
# Hello ksrn Good Morning
#
# Hello theja Good Morning
# Hello ksrn Bad Morning
