class library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lend={}
    def displaybooks(self):
        print(f"we have following books in our library: {self.name}")
        for book in self.booklist:
            print(book)
    def lendbook(self,user,book):
        if book not in self.lend.keys():
            self.lend.update({book:user})
            print("lendbook database has been updated,you can take a book now")
        else:
            print(f"book is alrady being used by {self.lend[book]}")
    def addbook(self,book):
        self.booklist.append(book)
        print("book has been added to booklist")
    def returnbook(self,book):
        self.lend.pop(book)
if __name__=='__main__':
    books = library(['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'], "Let's Upskill")
    while(True):
        print("welcome to the library ,please enter your choice")
        print("1 display books")
        print("2 lend a book")
        print("3 add a book")
        print("4 return a book")
        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            print("please enter a walid option")
            continue
        else:
            user_choice=int(user_choice)
        if user_choice==1:
            books.displaybooks()
        elif user_choice==2:
            book=input("enter the name of book, you want to lend")
            user=input("please enter your name")
            books.lendbook(user,book)
        elif user_choice==3:
            book=input("enter the name of the book you want to add: ")
            books.addbook(book)
        elif user_choice==4:
            book=input("enter the name of the book you want to return: ")
            books.returnbook(book)
        else:
            print("not a valid option")
        print("press q to quit and c to continue")
        user_choice2=""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2=input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue    



    
