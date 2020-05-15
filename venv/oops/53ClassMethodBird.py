class Bird:
    wings = 2

    @classmethod
    def fly(cls, name):
        print('{} flying with {} wings'.format(name, cls.wings))


Bird.fly('B1')
Bird.fly('B2')

# B1 flying with 2 wings
# B2 flying with 2 wings
