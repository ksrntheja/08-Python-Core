class P:
    def __init__(self):
        print('P Constructor')
        print(id(self))


class C(P):
    def __init__(self):
        # Call to __init__ of super class is missed
        print('C Constructor')
        print(id(self))


c = C()
print(id(c))

# C Constructor
# 140043215127496
# 140043215127496
