class Library:
    book_list = []

    def entry_book(self):
        book_info ={'book_id':self.book_id,'title':self.title,'author':self.author,'availability':self.availability}
        Library.book_list.append(book_info)

class Book:
    def __init__(self,book_id,title,author,availability):
        self.book_id = 100 + book_id
        self.title = title
        self.author = author
        self.availability = availability

    def borrow_book(id):
        found = False
        for books in Library.book_list:
            if(books['book_id'] == id):
                found = True
                if(books['availability']==True):
                    books['availability'] = False
                    print('Book has been successfully borrow\n')
                    break
                else:
                    print(f"Book with ID {id} is already borrowed")
                    print("\n")
                
        if not found:
            print('Invalid book ID')
            print("\n")


    def return_book(id):
        found = False
        for books in Library.book_list:
            if(books['book_id'] == id):
                found = True
                if(books['availability']==False):
                    books['availability'] = True
                    print(f"Book with ID {id} has been successfully returned.")
                    print("\n") 
                    break
                else:
                    print(f"Book with ID {id} is not borrowed,Its available")
                    print("\n")
        if not found:
            print('Invalid book ID')
            print("\n")

    def view_all_book():
        print("Books Library's")
        for books in Library.book_list:
            print(f"id:{books['book_id']} title: {books['title']} author:{books['author']} availability:{books['availability']}")
        print("\n")

book1 = Book(1,'SPL','Abdur',True)
Library.entry_book(book1)
book2 = Book(2,'Calculus','Motin',True)
Library.entry_book(book2)
book3 = Book(3,'Physics','David',True)
Library.entry_book(book3)
book4 = Book(4,'Statistics','Gupta',True)
Library.entry_book(book4)
book5 = Book(5,'DIgital System','Tocci',True)
Library.entry_book(book5)



while True:
    print("-----Rent a Book----\n\n1. View All Books\n2. Borrow Book\n3. Return Book\n4. Exit.\n")
    s = input("Enter your choice: ")
    print("\n")
    if(s=='1'):
        Book.view_all_book()
    elif(s=='2'):
        x=int(input("Enter book ID to borrow: "))
        Book.borrow_book(x)
    elif(s=='3'):
        x=int(input("Enter book ID to returned: "))
        Book.return_book(x)
    elif(s=='4'):
        break;    
    else:
        print('Enter valid option\n')