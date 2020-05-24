import inspect


def getInfo():
    # print(inspect.stack())
    # print(inspect.stack()[1])
    print('Caller module:', inspect.stack()[1][1])
    print('Caller function name:', inspect.stack()[1][3])
