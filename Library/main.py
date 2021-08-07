from tabulate import tabulate
from random import randint
import copy
from datetime import timedelta, date


class Library():

    def __init__(self):
        print("Welcome to Edyoda Library!")
        print(' ')
        inp9 = input("Do you want to see menu? Y/N: ")
        print("  ")
        if inp9.lower() == 'y':
            self.menu()
        else:
            print("You are free to wander!")

    def menu(self):
        key = True
        while key:
            print("  ")
            print('**********************************************')
            print("  ")
            print('Press 1: Register as User')
            print('Press 2: Login')
            print("Press 3: See Books in Library")
            print("Press 4: Admin Panel")
            print("Press 5: User Panel")
            print("Press 6: Exit!")
            print("  ")
            inp = input("Please Enter your response: ")
            print("  ")
            if inp == '1':
                print("  ")
                print('**********************************************')
                self.signUp()
            elif inp == '2':
                print("  ")
                print('**********************************************')
                self.login()
            elif inp == '3':
                print("  ")
                print('**********************************************')
                self.display_books()
            elif inp == '4':
                print("  ")
                print('**********************************************')
                print("  ")
                print("You are in Admin Panel")
                print("Press 1: Register as Admin")
                print("Press 2: Login as Admin")
                print("Press 3: Create a borrower")
                print("Press 4: Display all Admins")
                print("Press 5: Display all Users")
                print("Press 6: Display Users History")
                print("Press 7: Add New Book")
                print("Press 8: Edit Book")
                print("Press 9: Delete Book")
                print("  ")
                inp3 = input("Please Enter your response: ")
                print("  ")
                if inp3 == '1':
                    print("  ")
                    print('**********************************************')
                    self.adminSignUp()
                elif inp3 == '2':
                    print("  ")
                    print('**********************************************')
                    self.login()
                elif inp3 == '3':
                    print("  ")
                    print('**********************************************')
                    self.makeBorrower()
                elif inp3 == '4':
                    print("  ")
                    self.display_admins()
                    print(' ')
                elif inp3 == '5':
                    print("  ")
                    self.display_users()
                    print(" ")
                elif inp3 == '6':
                    print("  ")
                    self.userHistory()
                    print(" ")
                elif inp3 == '7':
                    print("  ")
                    print('**********************************************')
                    self.addBooks()
                elif inp3 == '8':
                    print("  ")
                    print('**********************************************')
                    self.edit_book()
                elif inp3 == '9':
                    print("  ")
                    print('**********************************************')
                    self.remove_book()
            if inp == '5':
                print("  ")
                print('**********************************************')
                print("  ")
                print("You are in Users Panel")
                print("Press 1: Issue Book")
                print("Press 2: My History")
                print("Press 3: Return Book")
                print("Press 4: Display Books")
                print("  ")
                inp4 = input("Please Enter your response: ")
                print("  ")
                if inp4 == '1':
                    print("  ")
                    print('**********************************************')
                    self.book_issue()
                elif inp4 == '2':
                    print("  ")
                    self.mybookshistory()
                    print("  ")
                elif inp4 == '3':
                    print("  ")
                    print('**********************************************')
                    self.returnBook()
                elif inp4 == '4':
                    print("  ")
                    self.display_books()
            if inp == '6':
                print("Thank you!")
                key = False

    # ****************************************************************************************************************************

    def random4digit(n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)

    def currentdate(self):
        Date_req = date.today()
        return Date_req

    users = [['Name', 'Email', 'Password', 'Role'], ['Admin', 'admin', 'admin', 'Admin']]
    books = [['BookID', 'Book Title', 'Author', 'Pages', 'No. of copies', 'ISBN', 'Published Year'],
             [random4digit(4), 'Rich Dad, Poor Dad', 'Robert Kiyosaki', 336, 5, random4digit(13), 2000],
             [random4digit(4), 'In Search of Lost Time', 'Marcel Proust', 4_215, 7, random4digit(13), 1913],
             [random4digit(4), 'Hamlet', 'William Shakespeare', 500, 12, random4digit(13), 1601],
             [random4digit(4), 'The Odyssey', 'Homer', 384, 6, random4digit(13), 1614],
             [random4digit(4), "Gulliver's Travels", 'Jonathan Swift', 350, 2, random4digit(13), 1726],
             [random4digit(4), 'Jyotipunj', 'Narendra Modi', 200, 9, random4digit(13), 2009]]
    books_history = [['Email', 'BookID', 'Book Title', 'Author', 'Pages', 'No. of copies', 'ISBN', 'Published Year',
                      'Date of Issue']]
    removedBooks = [['BookID', 'Book Title', 'Author', 'Pages', 'No. of copies', 'ISBN', 'Published Year']]

    active_user = [['Email', 'Password', 'Role'], ['Email', 'Password', 'Role']]

    def signUp(self):
        self.name = input("Enter your Full Name: ")
        self.age = input("Enter your Date of Birth: ")
        self.contact = input("Enter your Contact no.: ")
        self.email = input("Enter your Email: ")
        self.password = input("Enter your Password: ")
        self.role = 'Borrower'
        for i in range(len(self.users)):
            if self.email in self.users[i]:
                print(" ")
                print("User Already Exists")
                break
        else:
            self.users.append([self.name, self.email, self.password, self.role])
            print('User Registered Successfully')

    counter1 = 0

    def login(self):
        self.email = input("Please enter your registered email: ")
        self.password = input("Please enter your password: ")
        for i in self.users:
            if self.email in i and self.password in i:
                self.counter1 = 1
                self.active_user.clear()
                self.active_user.append(['Email', 'Password', 'Role'])
                self.active_user.append([i[1], i[2], i[3]])
            elif self.email == 'admin' and self.password == 'admin':
                self.counter1 = 1
                self.active_user.clear()
                self.active_user.append(['Email', 'Password', 'Role'])
                self.active_user.append(['admin', 'admin', 'Admin'])
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
        for i in range(len(self.users)):
            if self.email in self.users[i]:
                print(" ")
                print("Admin Already Exists")
                break
        else:
            self.users.append([self.username, self.email, self.password, self.role])
            print('Congratulations! You are an Admin now.')

    def display_admins(self):
        if self.active_user[1][2] == "Admin":
            adminlistindb = [['Name', 'Email', 'Password', 'Role']]
            for i in range(len(self.users)):
                if self.users[i][3] == "Admin":
                    adminlistindb.append(self.users[i])
            print(tabulate(adminlistindb, headers='firstrow', tablefmt='fancy_grid'))
        else:
            print("You need to be Admin to view this feature.")

    def display_users(self):
        if self.active_user[1][2] == "Admin":
            userlistindb = [['Name', 'Email', 'Password', 'Role']]
            for i in range(len(self.users)):
                if self.users[i][3] == "Borrower":
                    userlistindb.append(self.users[i])
            print(tabulate(userlistindb, headers='firstrow', tablefmt='fancy_grid'))
        else:
            print("You need to be Admin to view this feature.")

    def displayAllUsers(self):
        if self.active_user[1][2] == "Admin":
            print(tabulate(self.users, headers='firstrow', tablefmt='fancy_grid'))
        else:
            print("You need to be Admin to view this feature.")

    def makeAdmin(self):
        if self.active_user[1][2] == "Admin":
            self.name = input("Enter Username: ")
            self.email = input("Enter the Email: ")
            self.password = input("Enter password: ")
            self.role = 'Admin'
            for i in range(len(self.users)):
                if self.email in self.users[i]:
                    print(" ")
                    print("Admin Already Exists")
                    break
            else:
                self.counter2 = input("Do you want to give {0} Admin privilege? Y/N: ".format(self.name))
                if self.counter2 == 'Y' or self.counter2 == 'y':
                    print("{0} has been given Admin rights.".format(self.name))
                    self.users.append([self.name, self.email, self.password, self.role])
                else:
                    print("No Worries!")
        else:
            print("Please login first.")

    def makeBorrower(self):
        if self.active_user[1][2] == "Admin":
            self.name = input("Enter Full Name: ")
            self.age = input("Enter Date of Birth: ")
            self.contact = input("Enter Contact no.: ")
            self.email = input("Enter Email: ")
            self.password = input("Enter Password: ")
            self.role = 'Borrower'
            for i in range(len(self.users)):
                if self.email in self.users[i]:
                    print(" ")
                    print("User Already Exists")
                    break
            else:
                self.users.append([self.name, self.email, self.password, self.role])
                print('User Registered Successfully')
        else:
            print("Please login first.")

    @classmethod
    def addBooks(cls):
        if cls.active_user[1][2] == "Admin":
            bookId = cls.random4digit(4)
            bookTitle = input("Enter the Book Title: ")
            author = input("Enter the Authors name: ")
            pages = input("Enter No. of pages: ")
            noOfCopies = input("Enter No. of copies: ")
            isbn = input("Enter 13 digit ISBN Code: ")
            publishedYear = input("Enter Published Year: ")
            cls.books.append([bookId, bookTitle, author, pages, noOfCopies, isbn, publishedYear])
        else:
            print("Please login first")

    def book_issue(self):
        if self.active_user[1][2] == "Admin" or self.active_user[1][2] == 'Borrower':
            self.display_books()
            self.bookID = int(input("Enter Book ID: "))
            for j in range(1, len(self.books)):
                if self.bookID in self.books[j]:
                    print(self.books[j])
                    resp = input("Do you want to borrow this book? Y/N: ")
                    if resp.lower() == 'y':
                        if self.books[j][4] > 0:
                            print("Book Issued!")
                            self.books[j][4] -= 1
                            new_list = copy.deepcopy(self.books[j])
                            new_list.insert(0, self.active_user[1][0])
                            new_list[5] = 1
                            curr_date = date.today()
                            new_list.append(curr_date)
                            self.books_history.append(new_list)

                        else:
                            print("Book Out of Stock!")
                    else:
                        print("No Worries! Come again.")
                    break
            else:
                print('Book not found!')
        else:
            print("Please Login First.")

    columns = ['Email', 'BookID', 'Book Title', 'Author', 'Pages', 'No. of copies', 'ISBN', 'Published Year',
               'Date of issue']

    def mybookshistory(self):
        if self.active_user[1][2] == "Admin" or self.active_user[1][2] == 'Borrower':
            new_list3 = []

            for i in range(len(self.books_history)):
                if self.active_user[1][0] in self.books_history[i][0]:
                    new_list3.append(self.books_history[i])
            print(tabulate(new_list3, headers=self.columns, tablefmt='fancy_grid'))

    def remove_book(self):
        if self.active_user[1][2] == "Admin":
            self.display_books()
            inpa = int(input("Enter Book ID to remove: "))
            for j in range(len(self.books)):
                if inpa in self.books[j]:
                    print(self.books[j])
                    resp1 = input("Do you want to remove this book? Y/N: ")
                    if resp1.lower() == 'y':
                        removed = self.books.pop(j)
                        self.removedBooks.append(removed)
                        print("Book is removed from the Library")
                    else:
                        print("No Worries!")
                    break
            else:
                print("BookID not valid!")
        else:
            print("Please Login First.")

    def edit_book(self):
        if self.active_user[1][2] == "Admin":
            self.display_books()
            inpb = int(input("Enter Book ID to edit: "))
            for j in range(len(self.books)):
                if inpb in self.books[j]:
                    print(self.books[j])
                    resp1 = input("Do you want to edit this book? Y/N: ")
                    if resp1.lower() == 'y':
                        print("Press corresponding number to change.")
                        print("Press 1: Book Title")
                        print("Press 2: Author Name")
                        print("Press 3: Pages")
                        print("Press 4: No. of Copies")
                        print("Press 5: ISBN")
                        print("Press 6: Published Year")
                        inpc = input("Please enter your response: ")
                        if inpc == '1':
                            self.books[j][1] = input("Enter the new Book Title: ")
                            print("Changes Applied!")
                        if inpc == '2':
                            self.books[j][2] = input("Enter the new Author Name: ")
                            print("Changes Applied!")
                        if inpc == '3':
                            self.books[j][3] = input("Enter the new Pages: ")
                            print("Changes Applied!")
                        if inpc == '4':
                            self.books[j][4] = input("Enter the new No. of Copies: ")
                            print("Changes Applied!")
                        if inpc == '5':
                            self.books[j][5] = input("Enter the new ISBN code: ")
                            print("Changes Applied!")
                        if inpc == '6':
                            self.books[j][6] = input("Enter the new Published Year: ")
                            print("Changes Applied!")
                    else:
                        print("No Worries!")
                    break
            else:
                print("BookID not valid!")
        else:
            print("Please Login First.")

    def userHistory(self):
        if self.active_user[1][2] == "Admin":
            self.displayAllUsers()
            inpd = input("Enter Email ID of user: ")
            new_list2 = []
            new_list3 = []
            coun = []
            for j in range(len(self.users)):
                if inpd in self.users[j]:
                    print(self.users[j])
                    inpe = input("Do you want to check this user's history? Y/N: ")
                    if inpe.lower() == 'y':
                        for i in range(len(self.books_history)):
                            if inpd in self.books_history[i][0]:
                                coun.append('True')
                                new_list2 = copy.deepcopy(self.books_history[i])
                                new_list2[5] = 1
                                new_list3.append(new_list2)
                            else:
                                coun.append('False')

                        if 'True' in coun:
                            print(tabulate(new_list3, headers=self.columns, tablefmt='fancy_grid'))
                        else:
                            print("No browsing history!")
                    else:
                        print("No Worries!")
                    break
            else:
                print('Email ID not found!')
        else:
            print("Please Login First.")

    def returnBook(self):
        if self.active_user[1][2] == "Admin" or self.active_user[1][2] == 'Borrower':
            self.mybookshistory()
            yel = int(input("Enter the Id of Book to return: "))
            for i in range(len(self.books_history)):
                if yel in self.books_history[i] and self.active_user[1][0] in self.books_history[i]:
                    print(self.books_history[i][0:8])
                    inpde = input("Do you want to return this book? Y/N: ")
                    if inpde.lower() == 'y':
                        if self.currentdate() < self.books_history[i][-1] + timedelta(days=14):
                            self.books_history.pop(i)
                            print("You have successfully returned the book")
                        else:
                            print("You are late! You are fined ₹100 for late submission.")
                            self.books_history.pop(i)
                    else:
                        print("No worries!")
                    break
                else:
                    print("Book not found in User's history!")
        else:
            print("Please Login first!")

a= Library()