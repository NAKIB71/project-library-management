library = {
    "The Great Gatsby": [5, "F. Scott Fitzgerald"],
    "1984": [8, "George Orwell"],
    "To Kill a Mockingbird": [3, "Harper Lee"],
    "Pride and Prejudice": [4, "Jane Austen"]
}

def display_books():
    """Displays the available books in the library."""
    print("\nAvailable Books:")
    print("=" * 50)
    print(f"{'Book Title':<30}{'Quantity':<10}{'Author':<10}")
    print("=" * 50)
    for title, details in library.items():
        print(f"{title:<30}{details[0]:<10}{details[1]:<10}")
    print("=" * 50)

def add_new_book():
    """Adds a new book to the library."""
    title = input("Enter the title of the book: ").strip()
    if title in library:
        print(f"'{title}' already exists in the library.")
        return
    author = input("Enter the author of the book: ").strip()
    quantity = int(input("Enter the quantity: "))
    library[title] = [quantity, author]
    print(f"Book '{title}' by {author} added with {quantity} copies.")

def borrow_book():
    """Handles borrowing a book from the library."""
    title = input("Enter the title of the book you want to borrow: ").strip()
    if title not in library:
        print(f"Sorry, '{title}' is not available in the library.")
        return
    if library[title][0] > 0:
        library[title][0] -= 1
        print(f"You have successfully borrowed '{title}'.")
    else:
        print(f"Sorry, '{title}' is currently out of stock.")

def return_book():
    """Handles returning a book to the library."""
    title = input("Enter the title of the book you are returning: ").strip()
    if title not in library:
        print(f"'{title}' does not belong to this library. Please check again.")
        return
    library[title][0] += 1
    print(f"Thank you for returning '{title}'.")

def main():
    """Main menu for the library management system."""
    while True:
        print("\nLibrary Management System")
        print("1: Display Available Books")
        print("2: Add New Book")
        print("3: Borrow Book")
        print("4: Return Book")
        print("5: Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            display_books()
        elif choice == '2':
            add_new_book()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the library management system
if __name__ == "__main__":
    main()
