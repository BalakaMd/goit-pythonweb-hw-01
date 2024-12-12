from abc import ABC, abstractmethod


# SRP
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# ISP
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def show_books(self):
        pass


# OCP, LSP
class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, title: str):
        self.books = [book for book in self.books if book.title != title]

    def show_books(self):
        if not self.books:
            print("Library is empty.\n")
        else:
            for book in self.books:
                print(book)


# DIP
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str):
        book = Book(title, author, year)
        self.library.add_book(book)
        print(f"Book '{title}' added to the library.\n")

    def remove_book(self, title: str):
        self.library.remove_book(title)
        print(f"Book '{title}' removed from the library.\n")

    def show_books(self):
        print("\nLibrary contents:")
        self.library.show_books()
        print("\n")


def main():
    library = Library()
    manager = LibraryManager(library)
    try:
        while True:
            command = input("Enter command (add, remove, show, exit): ").strip().lower()

            match command:
                case "add":
                    title = input("Enter book title: ").strip()
                    author = input("Enter book author: ").strip()
                    year = input("Enter book year: ").strip()
                    manager.add_book(title, author, year)
                case "remove":
                    title = input("Enter book title to remove: ").strip()
                    manager.remove_book(title)
                case "show":
                    manager.show_books()
                case "exit":
                    break
                case _:
                    print("Invalid command. Please try again.\n")
    except KeyboardInterrupt:
        print("\nExiting the program.\n")

if __name__ == "__main__":
    main()