class bookshop:
    def __init__(self ,book_iD ,name_book ,name_Author ,number_book):
        self.book_iD = iD
        self.name_book = name
        self.name_Author = Author
        self.number_book = numbers
    def update_info(self, title, author, quantity):
        self.title = title
        self.author = author
        self.quantity = quantity
   def __str__(self):
        return f"book {self.title} by {self.author} , ID: {self.book_id} , Quantity: {self.quantity}"
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_iD, name_book, name_Author ,number_book):
        self.books.append(Book(book_iD, name_book, name_Author ,number_book))
        print("Book added successfully!")
         def view_books(self):
        if not self.books:
            print("\nNo books available.")
        else:
            print("\nLibrary Collection:")
            for index, book in enumerate(self.books, 1):
                print(f"{index}. {book}")

    def update_book(self, book_index):
        try:
            new_title = input("Enter new book title: ")
            new_author = input("Enter new author name: ")
            new_quantity = input("Enter new quantity: ")
            self.books[book_index - 1].update_info(new_title, new_author, new_quantity)
            print("Book updated successfully!")
        except IndexError:
            print("Invalid book number!")

    def remove_book(self, book_index):
        try:
            self.books.pop(book_index - 1)
            print("Book removed successfully!")
        except IndexError:
            print("Invalid book number!")


def main():
    library = Library()

    while True:
        print("\n Library Management:")
        print("1 - View All Books")
        print("2 - Add New Book")
        print("3 - Update Book")
        print("4 - Remove Book")
        print("5 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.view_books()
        elif choice == "2":
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            quantity = input("Enter quantity: ")
            library.add_book(book_id, title, author, quantity)
        elif choice == "3":
            book_index = int(input("Enter book number: "))
            library.update_book(book_index)
        elif choice == "4":
            book_index = int(input("Enter book number: "))
            library.remove_book(book_index)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

