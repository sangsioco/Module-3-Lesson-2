# to display catalog
def display_catalog(catalog):
    for book in catalog:
        print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}")

# to search by title
def search_by_title(catalog):
    title = input("Enter book title to search: ")
    found = False
    for book in catalog:
        if title.lower() in book[0].lower():
            print(f"Title: {book[0]}, Author: {book[1]}, Genre: {book[2]}")
            found = True
            break
    if not found:
        print("Book not found")

# to list by genre
def list_by_genre(catalog):
    genre = input("Enter genre to list books: ").lower()
    found = False
    for book in catalog:
        if genre == book[2].lower():
            print(f"Title: {book[0]}, Author: {book[1]}")
            found = True
    if not found:
        print("No books found in this genre")

# to add new book
def add_book_to_catalog(catalog):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    genre = input("Enter genre: ")
    new_book = (title, author, genre)
    for book in catalog:
        if new_book[:2] == book[:2]:  
            print("This book already exists in the library.")
            return False
    catalog.append(new_book)
    print("Book added successfully.")
    return True

def main():
    catalog = [
        ("1984", "George Orwell", "Dystopian"),
        ("Brave New World", "Aldous Huxley", "Dystopian")
    ]

    while True:
        print("\n1. View all books")
        print("2. Search book by title")
        print("3. List books by genre")
        print("4. Add a new book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_catalog(catalog)
        elif choice == '2':
            search_by_title(catalog)
        elif choice == '3':
            list_by_genre(catalog)
        elif choice == '4':
            add_book_to_catalog(catalog)
        elif choice == '5':
            print("Exiting library system")
            break
        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()
