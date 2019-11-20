"""
Name: Ding Yanjie
Date: Jan. 5th 2017
Brief introduction: This program lists and marks four books for users. In addition, users can also add books in the system. At the meanwhile, this program used seven functions to run.
Github link: https://github.com/ginhuand/Prgramming1Assessment1
"""

from operator import itemgetter
fileName = "books.csv"
fileList = []
file = "book"

class book:
	def __init__(self,info): # this function is to add local variables
		self.name=''
		self.author=''
		self.page=0
		self.status='r'
		if len(info)>=4:
			self.name=info[0]
			self.author=info[1]
			self.page=int(info[2])
			self.status=info[3] if len(info[3])==1 else info[3][0]
		self.status=self.status.lower()
	def toStr(self):
		return "%-50s\tby %-20s\t%d pages"%(self.name, self.author, self.page)

	
	
def read_file(books):# book list
	dataList=[]
	file_pointer= open(fileName, "r")
	for l in file_pointer.readlines():
		l = l.strip()
		datum = l.split(",")
		dataList.append(datum)
	dataList.sort(key=itemgetter(1, 2))
	file_pointer.close()
	for d in dataList:
		books.append(book(d))
	print("Reading List 1.0 - by Lindsay Ward \n%d books loaded from books.csv"%len(books))

def save_file(books): # Quit loop
	dataList=[]
	file_pointer= open(fileName, "w")
	for b in books:
		file_pointer.write("%s,%s,%d,%s\n"%(b.name,b.author,b.page,b.status))
	print("%d books saved to books.csv\nHave a nice day :)"%len(books))


def requiredBooks(books): # this function is to print Required books and sum up their pages
	totalPages=0
	bookCount=0
	print("Required books:")
	for i in range(len(books)):
		if books[i].status=='r':
			bookCount+=1
			totalPages+=books[i].page
			print("%d. %s"%(i,books[i].toStr()))
	if bookCount>0:
		print("Total pages for %d books: %d"%(bookCount,totalPages))
	else:
		print("No books")

def completeBooks(books): # this function is to print Completed books and sum up their pages
	totalPages=0
	bookCount=0
	print("Completed books:")
	for i in range(len(books)):
		if books[i].status=='c':
			bookCount+=1
			totalPages+=books[i].page
			print("%d. %s"%(i,books[i].toStr()))
	if bookCount>0:
		print("Total pages for %d books: %d"%(bookCount,totalPages))
	else:
		print("No books")
	
def markBook(books): # to mark the books
	count=0
	for b in books:
		if b.status=='r':
			count+=1
			break
	if count>0:
		requiredBooks(books)
	else:
		print("No required books")
		return
	print("Enter the number of a book to mark as completed")
	while True:
		try:
			bookIndex=int(input(">>>"))
			if bookIndex<0 or bookIndex>=len(books):
				return
			if books[bookIndex].status=='c':
				print("That book is already completed")
			else:
				books[bookIndex].status='c'
				print("%s by %s marked as completed"%(books[bookIndex].name,books[bookIndex].author))
			return
		except:
			print("Invalid input; enter a valid number")
	
def addBook(books):# this function is to add new book
	newBook=book([])
	while True:
		newBook.name=input("Title:").replace(" ","")
		if newBook.name=='':
			print("Input can not be blank")
		else:
			break
	while True:
		newBook.author=input("Author:").replace(" ","")
		if newBook.author=='':
			print("Input can not be blank")
		else:
			break
	while True:
		try:
			newBook.page=int(input("Pages:"))
			if newBook.page<0:
				print("Number must be >= 0")
			else:
				break
		except:
			print("Invalid input; enter a valid number")
	books.append(newBook)
	print("%s by %s, (%d pages) added to reading list"%(newBook.name,newBook.author,newBook.page))

read_file(fileList)

'''for f in fileList:
	print(f.toStr())'''

while True:# to print main menu and opitions
	mainMenu = "Menu:\nR - List required books\nC - List completed books\nA - Add new book\nM - Mark a book as completed\nQ - Quit"
	print(mainMenu)
	mainChoice = input(">>> ").upper()
	if mainChoice == "R":
		requiredBooks(fileList)
	elif mainChoice == "C":
		completeBooks(fileList)
	elif mainChoice == "M":
		markBook(fileList)
	elif mainChoice == "A":
		addBook(fileList)
	elif mainChoice == "Q":
		break
	else:
		print("Invalid menu choice")

save_file(fileList)
