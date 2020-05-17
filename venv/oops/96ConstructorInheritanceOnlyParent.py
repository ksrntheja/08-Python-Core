class P:
    def __init__(self):
        print('P Constructor')
        print(id(self))


class C(P):
    pass


c = C()
print(id(c))

# P Constructor
# 140507257111496
# 140507257111496
