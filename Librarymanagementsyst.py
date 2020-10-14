
class Library:
    d1 = {}

    def __init__(self, list_of_books, lib_name):
        self.book = list_of_books
        self.name = lib_name

    def display_book(self):
        for item in list_of_books:
            print(item)

    def lend_book(self):
        lend_name = input("Enter Your name")
        lend_book = input("enter the book you want to borrow")
        if lend_book in list_of_books:
            self.d1.update({lend_name: lend_book})
            list_of_books.remove(lend_book)
            # print(self.d1)
            print(f"{lend_name} borrowed {lend_book}")

        elif lend_book in self.d1.values():
            for key, value in self.d1.items():
                if value == lend_book:
                    print(f"The book you entered is not available. It is taken by the customer {key}")

        else:
            print("The book is not available in this library.Check out the others")

    def add_book(self):
        donate = input("Enter the name of the book you want to donate")
        list_of_books.append(donate)
        print(f"you have successfully donated {donate} book. Thank you for your contribution")

    def return_book(self):
        name = input("enter your name")
        back = input("Enter the book you want to return")
        if back in self.d1.values():
            for key, value in self.d1.items():
                if value == back:
                    self.d1.pop(key)
                    list_of_books.append(back)
                    break
            print(f"you have successfully returned the book {back}")
        else:
            print("you have entered the wrong book")


if __name__ == '__main__':

    user = 0
    list_of_books = ["percy jackson", "princess diary", "diary of wimpy kid", "4 hour work week", "scream", "around the world in 12 days",
             "alice in wonderland", "TVD", "50 shades of grey","The Secret", "Silence"]

    lib_name = "tejal"
    tejallib = Library(list_of_books, lib_name)

    while user != 'exit':
        user = input("Which action do you want to perform? Enter the no.\n1. Display all the books\n2. Lend a book\n"
                     "3. Donate a book\n4. Return a book\nEnter exit if you are done\n")
        if user == '1':
            tejallib.display_book()
            continue
        if user == '2':
            tejallib.lend_book()
            continue
        if user == '3':
            tejallib.add_book()
            continue
        if user == '4':
            tejallib.return_book()
            continue
        else:
            print("You've entered wrong values")
            continue




