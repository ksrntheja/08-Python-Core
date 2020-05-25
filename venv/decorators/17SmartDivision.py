def smart_division(func):
    def inner(a, b):
        print("We are dividing", a, "with", b)
        if b == 0:
            print("OOPS...cannot divide")
            return
        else:
            return func(a, b)

    return inner


@smart_division
def division(a, b):
    return a / b


print(division(20, 2))
print(division(20, 0))

# We are dividing 20 with 2
# 10.0
# We are dividing 20 with 0
# OOPS...cannot divide
# None
