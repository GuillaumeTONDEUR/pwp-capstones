class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.name + self.email

    def change_email(self, address):
        new_email = ""
        User.email = new_email
        print ("The new email was updated, now it's "+new_email)
        
    def __repr__(self):
        return print("User "+ self.name +", email: "+ self.email +", books read : " + str(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email
    
    def	__hash__(self):
        return	hash((self.title, self.isbn))
    
    def read_book(self, book, rating = None):
        self.books[book] = rating     
        
    def get_average_rating (self):
        sum_rating_book = 0 
        count = len(self.books)
        for i in self.books:
            sum_rating_book += i
        return sum_rating_book/count
    
class Books (object):
    def __init__(self,title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        
    def get_title(self): 
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print ("This news ISBN was updated, now it's "+ str(new_isbn))

    def add_rating (self, rating):
        if rating >= 0 and rating<=4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
            
    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn
    
    def get_average_rating (self):
        sum_rating_book = 0 
        count = len(self.rating)
        for i in self.rating:
            sum_rating_book += i
        return sum_rating_book/count
    
    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction (Books):
    def __init__(self,title, author, isbn):
        super().__init__(title,isbn)
        self.author = author
        
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return print(self.title +" by "+ self.author)
    
class Non_Fiction (Books):
    def __init__(self,title, subject, level, isbn):
        super().__init__(title,isbn)
        self.subject = subject
        self.level = level
        
    def get_subject (self):
        return self.subject 
    
    def get_level (self):
        return self.level 
        
    def __repr__(self):
        return print(self.title +", a "+self.level +" manual on "+ self.subject)        
    

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}
    
    def create_book (self, title, isbn):
        return Books(title,isbn)

    def create_novel (self, title, author, isbn):
        return Fiction(title, author, isbn)
    
    def create_non_fiction (self, title, subject, level, isbn):
        return Non_Fiction(title, subject,level, isbn)
    
    def add_book_to_user(self,book, email, rating = None):
        if email in self.users.keys():
            new_user = User(self.users[email],email)
            new_user.read_book(book,rating)
            new_book = Books(book.title,book.isbn)
            new_book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email {email}!".format(email=email))
    
    def add_user ( self, name ,email, user_books = None):
        new_user = User(name, email)
        self.users[email] = new_user 
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email , rating = 0)
    
    def print_catalog (self):
        print("List of books :")
        for book in self.books:
            print(book)
    
    def print_users(self):
        print("All of our user")
        for user in self.users:
            print(user)
            
    def most_read_book(self):
        name_book =""
        count_book = 0
        for book in self.books.keys():
            if self.books[book] > count_book:
                name_book = book.title
                count_book=self.books[book]
        return name_book,count_book
    
    def highest_rated_book (self):
        name_book =""
        rate_book = 0
        for book in self.books.keys():
            if book.get_average_rating()> rate_book:
                name_book = book.title
                rate_book = book.get_average_rating()
        return name_book, rate_book
    
    def most_positive_user(self):
        user_name =""
        user_rate=0
        for user in self.users.values():
            average = user.get_average_rating()
            if average>user_rate:
                user_name = user.name
                user_rate = average
        return user_name, user_rate
    
    
        


        
            
        


