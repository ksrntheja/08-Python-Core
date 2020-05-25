def decor(func):
    def inner(name):
        names = ['PM', 'CEO']
        if name in names:
            print("Hello {} Bad Morning".format(name))
        else:
            func(name)

    return inner


@decor
def wish(name):
    print("Hello", name, "Good Morning")


wish("theja")
wish("PM")
wish("ksrn")
wish("CEO")
wish("CEOO")

# Hello theja Good Morning
# Hello PM Bad Morning
# Hello ksrn Good Morning
# Hello CEO Bad Morning
# Hello CEOO Good Morning
