class Human:

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
head = human.Head()
head.talk()
brain = head.Brain()
brain.think()

# Hello.. Theja
# Talking...
# Thinking...
