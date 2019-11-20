from book import Book
from booklist import BookList

# test empty book (defaults)
book = Book("","",0,'r')
print(book)
assert book.author == ""
assert book.title == ""
assert book.pages == 0

# test initial-value book
book2 = Book("Fish fingers", "Dory", 2, 'r')

# test mark_completed()
book2.mark()
assert book2.flag == 'c'

bl = BookList()
bl.add_book(book2)
assert len(bl.completelist) == 1
book3 = Book("Simple",'Hegns',100,'r')
bl.add_book(book3)
assert len(bl.requirelist) == 1
bl.complete_book(book3)
assert len(bl.completelist) == 2

print("all tests passed!")