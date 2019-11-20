"""
Name: Ding Yanjie
Date: Jan. 26th 2017
Brief Project Description: Create a GUI version of the program I made in assignment 1, using Python 3 and the Kivy toolkit, as described in the following information and accompanying screencast. This assignment will display classes, GUIs, selection, repetition, exceptions, lists, file I/O and functions.
GitHub URL: https://github.com/ginhuand/CP1404ProgrammingAssessment2
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
import operator  
import csv  
from booklist import BookList
from book import Book

class BookReadList(App):
    def build(self):  # Create the main widget for Kivy program
        self.booklist = BookList()
        self.booklist.load_books()


        self.title = "Reading List 2.0"   # Kivy title
        self.root = Builder.load_file("app.kv")  # load Kivy
        self.loading()  # load the books
        return self.root

    def loading(self):  
        count = 0
        total = 0

        self.root.ids.entriesBox.clear_widgets()  # clear all the widgets

        self.root.ids.status_label.text = "Click books to mark them as completed" 

        for item in self.booklist.requirelist:  
            temp_button = Button(text=item.title, background_color=[count-0.5, 0, 1, 1])  # setting background colour
            temp_button.book = item
            temp_button.bind(on_release=self.handle_mark)  # if click display the list
            self.root.ids.entriesBox.add_widget(temp_button)
            count += 1
            
        total = self.booklist.getRequirePage()
        if count == 0:  # Situation when no book there
            self.root.ids.top_label.text = "No required items"  # Show the prompt at the top label
            self.root.ids.entriesBox.clear_widgets()  # Clear the list widgets
        else:  # Else print total price at the top label
            self.root.ids.top_label.text = "Total pages to read: {}".format(total)
            # Else show the total price of required items at top babel

    def handle_mark(self, book):  # Function when user click the button of the required item (Each required button)
        name = book.text
        self.booklist.complete_book(book.book)  # Using "c" instead of "r" in the list when user chooses the item
        self.root.ids.status_label.text = ("{} marked as completed".format(name))  # Show the marked item at the status label

    def completed(self):  # Function for the completed item (Completed button)
        count = 0
        total = 0

        self.root.ids.entriesBox.clear_widgets()  # Clear the list widgets

        for book in self.booklist.completelist:  # using for loop to separate to sorted file
          
            temp_button = Button(text=book.title)  # Setting the button text
            temp_button.book = book
            temp_button.bind(on_release=self.handle_completed)  # Setting when user click the button
            self.root.ids.entriesBox.add_widget(temp_button)  # Add widgets for each completed item
            count += 1
        total = self.booklist.getCompletePage()
        if count == 0:  # If total count = 0, then means no completed item
            self.root.ids.top_label.text = "No completed items"  # Show the prompt at the top label
            self.root.ids.entriesBox.clear_widgets()  # Clear the list widgets
        else:
            self.root.ids.top_label.text = "Total pages completed: {}".format(total)
            # Else show the total price of completed items at top babel

    def handle_completed(self, book):  # Function when user click the button of the completed item (Each conpleted button)
        self.root.ids.status_label.text = "{},write by {}, pages:{}, (completed)".format(book.book.title, book.book.author, book.book.pages)
        # Show the detail of the completed item at the status label

    def handle_add(self):  # Function for adding new item  (Add item button)
        title = self.root.ids.input_name.text  # Let user enter the item name
        author = self.root.ids.input_author.text  # Let user enter the pages of item
        pages = self.root.ids.input_pages.text  # Let user enter the priority of item

        if title == "" or pages == "" or author == "":  # If any field is blank, show error prompt
            self.root.ids.status_label.text = "All fields must be completed"
        else:
            try:  # Using exception let user enter valid number
                author = self.root.ids.input_author.text
                pages = int(self.root.ids.input_pages.text)
            except ValueError:
                self.root.ids.status_label.text = "Please enter a valid number"
            else:
                if pages <= 0:
                    self.root.ids.status_label.text = "pages must be >= 0"
                else:
                    book = Book(title, author, pages, flag='r')
                    self.booklist.add_book(book)
                    self.root.ids.status_label.text = "book \'{}\' wrote by {} in {} pages has been add to book list".format(title, author ,pages)
                    # show the added item at the status label
                    self.root.ids.input_name.text = ""
                    self.root.ids.input_author.text = ""
                    self.root.ids.input_pages.text = ""
                    # Clear whole input box after the new item add to the list
        # Error check

    def handle_clear(self):  # Function for clear whole input box (Clear button)
        self.root.ids.input_name.text = ""
        self.root.ids.input_author.text = ""
        self.root.ids.input_pages.text = ""

    def save_item(self):  # Function for saving completed item to the file (Save item button)
        file_writer = open("books.csv", "w")  # Open the file with the correct format
        count = 0
        writer = csv.writer(file_writer)
        for book in self.booklist.requirelist:
            writer.writerow([book.title, book.author, book.pages, book.flag])
            count += 1
        for book in self.booklist.completelist:
            writer.writerow([book.title, book.author, book.pages, book.flag])
            count += 1
        self.root.ids.status_label.text = "{} items saved to items.csv".format(count)
        # Display how many items which add to the file at the status label
        file_writer.close()
        # Close the file
if __name__ == "__main__":
    BookReadList().run()
