"""
Important OOP Methods: __init__, __str__, __repr__, __eq__
"""

# Yeh class Book object banane ke liye hai
class Book:
    def __init__(self, title, author):  # Constructor
        self.title = title
        self.author = author

    def __str__(self):  # Human-readable string representation
        return f"'{self.title}' by {self.author}"

    def __repr__(self):  # Developer-focused representation
        return f"Book(title={self.title}, author={self.author})"

    def __eq__(self, other):  # Equality check
        return self.title == other.title and self.author == other.author

book1 = Book("1984", "George Orwell")
book2 = Book("1984", "George Orwell")
book3 = Book("Animal Farm", "George Orwell")

print(str(book1))        # __str__ call
print(repr(book2))       # __repr__ call
print(book1 == book2)    # __eq__ call
print(book1 == book3)


print("This program was developed by Engr. Muhammad Javed.")
