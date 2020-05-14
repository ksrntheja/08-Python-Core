class Test:
    def __init__(self):
        print('id(self)->', id(self))


t = Test()
print('id(t)->', id(t))

# id(self)-> 140140544998256
# id(t)-> 140140544998256
