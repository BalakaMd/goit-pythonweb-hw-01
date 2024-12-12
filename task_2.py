import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    format="\n%(message)s",
    level=logging.DEBUG,
)


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
            logging.info("Library is empty.")
        else:
            for book in self.books:
                logging.info(book)


# DIP
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str):
        book = Book(title, author, year)
        self.library.add_book(book)
        logging.info(f"Book '{title}' added to the library.")

    def remove_book(self, title: str):
        self.library.remove_book(title)
        logging.info(f"Book '{title}' removed from the library.")

    def show_books(self):
        logging.info("Library contents:")
        self.library.show_books()
        logging.info("")


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
                    logging.info("Invalid command. Please try again.")
    except KeyboardInterrupt:
        logging.info("Exiting the program.")


if __name__ == "__main__":
    main()
