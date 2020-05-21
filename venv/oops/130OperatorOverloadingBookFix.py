class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        print('self.pages  :', self.pages)
        print('other.pages :', other.pages)
        return self.pages + other.pages


book01 = Book(100)
book02 = Book(200)
book03 = Book(300)
print('The total number of pages [book01 + book02] :', book01 + book02)
print('The total number of pages [book01 + book02 + book03] :', book01 + book02 + book03)

# self.pages  : 100
# other.pages : 200
# The total number of pages [book01 + book02] : 300
# self.pages  : 100
# other.pages : 200
# Traceback (most recent call last):
#   File "/Code/venv/oops/130OperatorOverloadingBookFix.py", line <>, in <module>
#     print('The total number of pages [book01 + book02 + book03] :', book01 + book02 + book03)
# TypeError: unsupported operand type(s) for +: 'int' and 'Book'
