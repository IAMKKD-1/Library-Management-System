from tabulate import tabulate
from random import randint


class User:
    def __init__(self, role, name=None, age=None, email=None):
        self.role = role
        self.name = name
        self.age = age
        self.email = email


class Library():
    users = [['Name', 'Email', 'Password']]
    books = [['BookID', 'Book Title', 'Author', 'Pages', 'No. of copies', 'ISBN', 'Published Year']]

    def __init__(self, user=User(role='Visitor')):
        if user.role == 'Visitor':
            self.limited_access = True

    def signUp(self):
        self.name = input("Enter your Full Name: ")
        self.age = input("Enter your Date of Birth: ")
        self.contact = input("Enter your Contact no.: ")
        self.email = input("Enter your Email: ")
        self.password = input("Enter your Password: ")
        self.users.append([self.name, self.email, self.password])
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

    def book_issue(self):
        self.toIssue = input("Enter book name: ")
        self.toID = input("Enter first 3 digits of ISBN code: ")
        if self.book_name_issue not in library.book_issued:
            print('{} issued to student Id {}'.format(self.book_name_issue, self.student_Id))
            library.book_issued.append(self.book_name_issue)
        else:
            print('book is already issued')


class Addbook:
    def he(self):
        self.bookId = self.random4digit(4)
        self.bookTitle = input("Enter the Book Title: ")
        self.author = input("Enter the Authors name: ")
        self.pages = input("Enter No. of pages: ")
        self.noOfCopies = input("Enter No. of copies: ")
        self.isbn = input("Enter 13 digit ISBN Code: ")
        self.publishedYear = input("Enter Published Year: ")
        self.books.append(
            [self.bookId, self.bookTitle, self.author, self.pages, self.noOfCopies, self.isbn, self.publishedYear])


class Admin(Library, User, Addbook):
    admin = [['Username', 'Email', 'Password']]
    counter = 0

    def __init__(self, user=User(role='Visitor')):
        if user.role == 'Visitor':
            self.limited_access = True

    def adminSignUp(self):
        self.role = 'Admin'
        self.username = input("Enter your Userame: ")
        self.email = input("Enter your Email: ")
        self.password = input("Enter your Password: ")
        self.admin.append([self.username, self.email, self.password])
        print('Congratulations! You are an Admin now.')

    @staticmethod
    def adminLogin(self):
        self.email = input("Please enter your registered email: ")
        self.password = input("Please enter your password: ")
        for i in self.admin:
            if (self.email in i and self.password in i):
                self.counter1 = 1
                break
            else:
                self.counter1 = 0

        if self.counter1 == 1:
            print("Welcome! You are successfully logged in.")
            self.limited_access = False
            role = 'Admin'
        elif self.counter1 == 0:
            print("User not found! Please Register.")
            self.limited_access = True

    def display_admins(self):
        print(tabulate(self.admin, headers='firstrow', tablefmt='fancy_grid'))

    def random4digit(self, n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)

    def display_users(self):
        print(tabulate(self.users, headers='firstrow', tablefmt='fancy_grid'))

    def makeAdmin(self):
        if self.limited_access == False:
            self.name = input("Enter Username: ")
            self.email = input("Enter the Email: ")
            self.password = input("Enter password: ")
            self.counter2 = input("Do you want to give {0} Admin privilege? Y/N: ".format(self.name))
            if self.counter2 == 'Y' or self.counter2 == 'y':
                print("{0} has been given Admin rights.".format(self.name))
                self.admin.append(self.name, self.email, self.password)
            else:
                print("No Worries!")
        else:
            print("Please Login first.")
