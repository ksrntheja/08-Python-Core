def marriagedecor(func):
    def inner():
        print('Hair decoration...')
        print('Face decoration with Platinum package')
        print('Fair and Lovely etc..')
        func()

    return inner


def getready():
    print('Ready for the marriage')


decorated_getready = marriagedecor(getready)

decorated_getready()

# Hair decoration...
# Face decoration with Platinum package
# Fair and Lovely etc..
# Ready for the marriage
