class P:
    def __init__(self):
        print('P constructor')


class C(P):
    def __init__(self):
        super().__init__()
        print('C constructor')


c = C()

# P constructor
# C constructor
