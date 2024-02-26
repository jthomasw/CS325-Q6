class BookCatalog:
    def add_book(self, book):
        print("Book added to the catalog.")

    def remove_book(self, book):
        print("Book removed from the catalog.")

    def search_by_title(self, title):
        print("Searching for books by title:", title)

    def search_by_author(self, author):
        print("Searching for books by author:", author)

    def search_by_genre(self, genre):
        print("Searching for books by genre:", genre)

class BookManagement:
    def borrow_book(self, book, user):
        print("Book borrowed by user:", user)

    def return_book(self, book, user):
        print("Book returned by user:", user)

class ReportGeneration:
    def generate_borrowing_report(self):
        print("Generating borrowing report.")

    def generate_overdue_report(self):
        print("Generating overdue report.")

    def generate_popularity_report(self):
        print("Generating popularity report.")

class Library(BookCatalog, BookManagement, ReportGeneration):
    def __init__(self):
        print("Library instance created.")

class GuestUser(BookCatalog):
    def search_by_title(self, title):
        print("Guest user searching for books by title:", title)

    def search_by_author(self, author):
        print("Guest user searching for books by author:", author)

    def search_by_genre(self, genre):
        print("Guest user searching for books by genre:", genre)

class Librarian(Library):
    def add_book(self, book):
        print("Book added to the library by librarian.")

    def remove_book(self, book):
        print("Book removed from the library by librarian.")

    def generate_borrowing_report(self):
        print("Generating borrowing report for librarian.")

    def generate_overdue_report(self):
        print("Generating overdue report for librarian.")

    def generate_popularity_report(self):
        print("Generating popularity report for librarian.")

def main():
    library = Library()
    guest_user = GuestUser()
    librarian = Librarian()

    library.add_book("Book 1")
    library.borrow_book("Book 2", "User 1")
    librarian.generate_borrowing_report()
    guest_user.search_by_author("Author Name")

if __name__ == "__main__":
    main()