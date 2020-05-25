def decor(func):
    def inner():
        print('Send the person to beauty parlour')
        print('Showing a person with full of makeup')

    return inner


@decor
def diaplay():
    print('Showing a person as it is')


diaplay()

# Send the person to beauty parlour
# Showing a person with full of makeup
