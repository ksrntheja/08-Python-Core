class P:
    def __init__(self):
        print('P constructor')


class C(P):
    def __init__(self):
        # Call to __init__ of super class is missed
        print('C constructor')


c = C()

# C constructor
