class P:
    def __init__(self):
        print('P Constructor')
        print(id(self))


class C(P):
    def __init__(self):
        super().__init__()
        print('C Constructor')
        print(id(self))


c = C()
print(id(c))

# P Constructor
# 140369570811296
# C Constructor
# 140369570811296
# 140369570811296
