from tabulate import tabulate
from random import randint
import time


class Library():

    def __init__(self):
        print("Welcome to Edyoda Library!")
        time.sleep(0.5)
        print('Press 1: Register')
        time.sleep(0.5)
        print('Press 2: Login')
        time.sleep(0.5)
        print("Press 3: See Books in Library")
        time.sleep(0.5)
        print("Press 4: No thanks!")
        time.sleep(0.5)
        inp = input("Please Enter your response: ")
        if inp == '1':
            print("Loading...")
            time.sleep(1)
            self.signUp()
        elif inp == '2':
            print("Loading...")
            time.sleep(1)
            self.login()
        elif inp == '3':
            print("Loading...")
            time.sleep(1)
            self.display_books()
        elif inp == '4':
            print("You can roam freely!")

    def random4digit(n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)

    users = [['Name', 'Email', 'Password', 'Role'], ['Admin', 'admin', 'admin', 'Admin'],
             ['User', 'user', 'user', 'Borrower']]
    #     ready_made_loginId = ['Admin','admin','admin','Admin'],['User','user','user','Borrower']
    books = [['BookID', 'Book Title', 'Author', 'Pages', 'No. of copies', 'ISBN', 'Published Year'],
             [random4digit(4), 'Rich Dad, Poor Dad', 'Robert Kiyosaki', 336, 5, random4digit(13), 2000],
             [random4digit(4), 'In Search of Lost Time', 'Marcel Proust', 4_215, 7, random4digit(13), 1913],
             [random4digit(4), 'Hamlet', 'William Shakespeare', 500, 12, random4digit(13), 1601],
             [random4digit(4), 'The Odyssey', 'Homer', 384, 6, random4digit(13), 1614],
             [random4digit(4), "Gulliver's Travels", 'Jonathan Swift', 350, 2, random4digit(13), 1726],
             [random4digit(4), 'Jyotipunj', 'Narendra Modi', 200, 9, random4digit(13), 2009]]

    def signUp(self):
        self.name = input("Enter your Full Name: ")
        self.age = input("Enter your Date of Birth: ")
        self.contact = input("Enter your Contact no.: ")
        self.email = input("Enter your Email: ")
        self.password = input("Enter your Password: ")
        self.role = 'Borrower'
        self.users.append([self.name, self.email, self.password, self.role])
        print('User Registered Successfully')

    counter1 = 0

    def login(self):
        self.email = input("Please enter your registered email: ")
        self.password = input("Please enter your password: ")
        for i in self.users:
            if (self.email in i and self.password in i):
                self.counter1 = 1
                break
            else:
                self.counter1 = 0

        if self.counter1 == 1:
            print("Welcome! You are successfully logged in.")

        elif self.counter1 == 0:
            print("User not found! Please Register.")

    def display_books(self):
        print(tabulate(self.books, headers='firstrow', tablefmt='fancy_grid'))

    def adminSignUp(self):
        self.role = 'Admin'
        self.username = input("Enter your Userame: ")
        self.email = input("Enter your Email: ")
        self.password = input("Enter your Password: ")
        self.users.append([self.username, self.email, self.password, self.role])
        print('Congratulations! You are an Admin now.')

    def display_admins(self):
        adminlistindb = [['Name', 'Email', 'Password', 'Role']]
        for i in range(1, len(self.users)):
            if self.users[i][3] == "Admin":
                adminlistindb.append(self.users[i])
        print(tabulate(adminlistindb, headers='firstrow', tablefmt='fancy_grid'))

    def display_users(self):
        userlistindb = [['Name', 'Email', 'Password', 'Role']]
        for i in range(1, len(self.users)):
            if self.users[i][3] == "Borrower":
                userlistindb.append(self.users[i])

        print(tabulate(userlistindb, headers='firstrow', tablefmt='fancy_grid'))

    def makeAdmin(self):
        for i in range(1, len(self.users)):
            if self.users[i][3] == "Admin":
                self.name = input("Enter Username: ")
                self.email = input("Enter the Email: ")
                self.password = input("Enter password: ")
                self.role = 'Admin'
                self.counter2 = input("Do you want to give {0} Admin privilege? Y/N: ".format(self.name))
                if self.counter2 == 'Y' or self.counter2 == 'y':
                    print("{0} has been given Admin rights.".format(self.name))
                    self.users.append([self.name, self.email, self.password, self.role])
                else:
                    print("No Worries!")
                break
            else:
                print("Please login first.")

    def makeBorrower(self):
        for i in range(1, len(self.users)):
            if self.users[i][3] == "Admin":
                self.name = input("Enter Full Name: ")
                self.age = input("Enter Date of Birth: ")
                self.contact = input("Enter Contact no.: ")
                self.email = input("Enter Email: ")
                self.password = input("Enter Password: ")
                self.role = 'Borrower'
                self.users.append([self.name, self.email, self.password, self.role])
                print('User Registered Successfully')
                break
            else:
                print("Please login first.")

    def addBooks(self):
        for i in range(1, len(self.users)):
            if self.users[i][3] == "Admin":
                self.bookId = self.random4digit(4)
                self.bookTitle = input("Enter the Book Title: ")
                self.author = input("Enter the Authors name: ")
                self.pages = input("Enter No. of pages: ")
                self.noOfCopies = input("Enter No. of copies: ")
                self.isbn = input("Enter 13 digit ISBN Code: ")
                self.publishedYear = input("Enter Published Year: ")
                self.books.append([self.bookId, self.bookTitle, self.author, self.pages, self.noOfCopies, self.isbn,
                                   self.publishedYear])
                break
            else:
                print("Please login first")

    def book_issue(self):
        for i in range(1, len(self.users)):
            if self.users[i][3] == "Admin" or self.users[i][3] == "Borrower":
                self.display_books()
                self.bookID = int(input("Enter Book ID: "))
                for j in range(1, len(self.books)):
                    if self.bookID in self.books[j]:
                        print(self.books[j])
                        time.sleep(1)
                        resp = input("Do you want to borrow this book? Y/N: ")
                        if resp.lower() == 'y':
                            if self.books[j][4] > 0:
                                print("Book Issued!")
                                self.books[j][4] -= 1
                            else:
                                print("Book Out of Stock!")
                        else:
                            print("No Worries! Come again.")
                        break
                else:
                    print('Book not found!')
                break
        else:
            print("Please Login First.")

