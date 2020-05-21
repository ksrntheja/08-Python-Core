class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        print('self.pages  :', self.pages)
        print('other.pages :', other.pages)
        return Book(self.pages + other.pages)


book01 = Book(100)
book02 = Book(200)
book03 = Book(500)
print('The total number of pages [book01 + book02] :', book01 + book02)
print('The total number of pages [book01 + book02 + book03] :', book01 + book02 + book03)

# self.pages  : 100
# other.pages : 200
# The total number of pages [book01 + book02] : <__main__.Book object at 0x7ff41c54cc50>
# self.pages  : 100
# other.pages : 200
# self.pages  : 300
# other.pages : 500
# The total number of pages [book01 + book02 + book03] : <__main__.Book object at 0x7ff41c553198>
