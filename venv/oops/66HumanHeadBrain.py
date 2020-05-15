class Human:

    def __init__(self):
        self.name = 'Theja'
        self.head = self.Head()
        self.brain = self.Brain()

    def display(self):
        self.name = 'Theja'
        print("Hello..", self.name)

    class Head:
        def talk(self):
            print('Talking...')

    class Brain:
        def think(self):
            print('Thinking...')


human = Human()
human.display()
human.head.talk()
human.brain.think()

# Hello.. Theja
# Talking...
# Thinking...
