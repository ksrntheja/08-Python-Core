class Constructor:
    def __init__(self):
        print('Constructor execution...')


c = Constructor()
print(c.__init__())
c.__init__()
c.__init__()

# Constructor execution...
# Constructor execution...
# None
# Constructor execution...
# Constructor execution...
