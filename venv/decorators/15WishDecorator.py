def decor(func):
    def inner(name):
        if name == "ksrn":
            print("Hello ksrn Bad Morning")
        else:
            func(name)

    return inner


@decor
def wish(name):
    print("Hello", name, "Good Morning")


wish("theja")
wish("ksrn")

# Hello theja Good Morning
# Hello ksrn Bad Morning
