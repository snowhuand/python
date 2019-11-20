# create your booklist class in this file
import csv
from book import Book


class BookList:
	def __init__(self):
		self.requirelist = []
		self.completelist = []
		self.require_pages = 0
		self.complete_pages = 0

	def add_book(self,book):
		if book.flag == 'r':
			self.requirelist.append(book)
			self.require_pages += book.pages
		else:
			self.completelist.append(book)
			self.complete_pages += book.pages

	def complete_book(self, book):
		try:
			self.requirelist.remove(book)
		except:
			for i in self.requirelist:
				print(i)
		self.completelist.append(book)
		self.require_pages -= book.pages
		self.complete_pages += book.pages
		book.mark()

	def getBookByTitle(self, title):
		for book in self.requirelist:
			if book.title == title:
				return book
		for book in self.completelist:
			if book.title == title:
				return book

	def load_books(self):
		with open('books.csv','r') as f:
			file_reader = csv.reader(f)
			for line in file_reader:
				b = Book(line[0],line[1],int(line[2]),flag=line[3])
				self.add_book(b)

	def save_books(self):
		with open('books.csv','w') as f:
			file_writer = csv.writer(f)
			for b in self.requirelist:
				file_writer.writerow([self.title, self.author, self.pages, self.flag])

	def sort(self):
		self.completelist.sort(key=lambda x:x.pages)
		self.requirelist.sort(key=lambda x:x.pages)

	def getCompletePage(self):
		return self.complete_pages

	def getRequirePage(self):
		return self.require_pages

