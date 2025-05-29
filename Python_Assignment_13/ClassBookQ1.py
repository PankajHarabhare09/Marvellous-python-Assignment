class Book:
    No_Of_Books = 0
    def __init__(self , name , author):
        self.Name = name
        self.Author = author
        self.No_Of_Books = (self.No_Of_Books + 1)

    def Display(self):
        print("Book Name: " , self.Name)
        print("Book Author: ",self.Author)
        print("No of Books: ",self.No_Of_Books)

def main():
    Bobj1 = Book("Linux System Programming" , "Robert Love")
    Bobj1.Display()

    Bobj2 = Book("C Programming Language" , "Danis Richert")
    Bobj2.Display()

if __name__ == "__main__":
    main()

'''
OUTPUT
Book Name:  Linux System Programming
Book Author:  Robert Love
No of Books:  1
Book Name:  C Programming Language
Book Author:  Danis Richert
No of Books:  1
'''