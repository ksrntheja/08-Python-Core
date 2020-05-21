class Book:
    def __init__(self, pages):
        self.pages = pages


book01 = Book(100)
book02 = Book(200)
print(book01 + book02)

# Traceback (most recent call last):
#   File "/Code/venv/oops/129OperatorOverloadingBook.py", line <>, in <module>
#     print(book01 + book02)
# TypeError: unsupported operand type(s) for +: 'Book' and 'Book'
