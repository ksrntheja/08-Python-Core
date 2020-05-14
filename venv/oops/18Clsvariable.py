class Cls:
    @classmethod
    def printIdCls(cls):
        print(id(cls))


print('id(Cls)          ->', id(Cls))
print('Cls.printIdCls() ->')
Cls.printIdCls()

# id(Cls)          -> 25449640
# Cls.printIdCls() ->
# 25449640
