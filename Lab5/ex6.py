class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def display_info(self):
        return f"Item ID: {self.item_id}, Title: {self.title}, Author: {self.author}, Checked Out: {self.checked_out}"

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            return f"{self.title} has been checked out."
        else:
            return f"{self.title} is already checked out."

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} is not checked out."


class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id)
        self.genre = genre

    def display_info(self):
        return super().display_info() + f", Genre: {self.genre}"


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.director = director
        self.duration = duration

    def display_info(self):
        return super().display_info() + f", Director: {self.director}, Duration: {self.duration} minutes"


class Magazine(LibraryItem):
    def __init__(self, title, issue_number, item_id):
        super().__init__(title, "Unknown", item_id)
        self.issue_number = issue_number

    def display_info(self):
        return super().display_info() + f", Issue Number: {self.issue_number}"


def main():
    # Example usage:
    book = Book("The 5th Wave ", "Rick Yancey", 578, "Post-apocalyptic")
    dvd = DVD("Jandarmul din Saint-Tropez", "Jean Girault", 21, 90)
    magazine = Magazine("National Geographic", 50, 788)

    print(book.display_info())
    print(book.check_out())
    print(book.display_info())
    print(book.check_out())
    print(book.return_item())
    print(book.display_info())

    print("\n-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/\n")

    print(dvd.display_info())
    print(dvd.check_out())
    print(dvd.display_info())
    print(dvd.return_item())
    print(dvd.display_info())

    print("\n-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/\n")

    print(magazine.display_info())
    print(magazine.check_out())
    print(magazine.display_info())
    print(magazine.return_item())
    print(magazine.display_info())


if __name__ == "__main__":
    main()
