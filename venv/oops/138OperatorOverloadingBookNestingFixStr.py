class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        print('+')
        print('self.pages  :', self.pages)
        print('other.pages :', other.pages)
        return Book(self.pages + other.pages)

    def __mul__(self, other):
        print('*')
        print('self.pages  :', self.pages)
        print('other.pages :', other.pages)
        return Book(self.pages * other.pages)

    def __str__(self):
        return 'The total number of pages: {}'.format(self.pages)


book01 = Book(100)
book02 = Book(200)
book03 = Book(500)
print('The total number of pages [book01 + book02] :', book01 + book02)
print('The total number of pages [book01 + book02 + book03] :', book01 + book02 + book03)
book04 = Book(50)
print('The total number of pages [book01 + book02 * book03 + book04] :', book01 + book02 * book03 + book04)

# +
# self.pages  : 100
# other.pages : 200
# The total number of pages [book01 + book02] : The total number of pages: 300
# +
# self.pages  : 100
# other.pages : 200
# +
# self.pages  : 300
# other.pages : 500
# The total number of pages [book01 + book02 + book03] : The total number of pages: 800
# *
# self.pages  : 200
# other.pages : 500
# +
# self.pages  : 100
# other.pages : 100000
# +
# self.pages  : 100100
# other.pages : 50
# The total number of pages [book01 + book02 * book03 + book04] : The total number of pages: 100150
