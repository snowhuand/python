# create your simple Book class in this file
class Book:
    def __init__(self, title, author, pages, flag='r'):
        self.title = title
        self.author = author
        self.pages = int(pages)
        self.flag = flag
    def __str__(self):
        return self.title

    def islong(self):
        return self.pages >= 500

    def mark(self):
        self.flag = 'c'
        