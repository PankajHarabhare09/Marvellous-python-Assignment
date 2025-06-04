class Book:
    def __init__(self , name , author , price):
        self.Bname = name
        self.Bauthor = author
        self.__Bprice = price

    def DisplayBookDetails(self):
        print("Book Name is: ",self.Bname)
        print("Book Author is: ",self.Bauthor)
        print("Book Price is: ",self.__Bprice)

def main():
    Bobj = Book("Let's C" , "ABC" , 450.50)
    Bobj.DisplayBookDetails()

    print(Bobj.Bname)
    print(Bobj.Bauthor)

    '''print(Bobj.__Bprice)
    THIS ERROR IS SHOWS THE WE CANNOT SHOW PRIVATE VARIABLE OUTSSIDE THE CLASS
    Traceback (most recent call last):
    File "C:\Users\ganes\Desktop\Python_Assignment_14\BookClassQ3.py", line 21, in <module>
    main()
    File "C:\Users\ganes\Desktop\Python_Assignment_14\BookClassQ3.py", line 18, in main
    print(Bobj.__Bprice)
          ^^^^^^^^^^^^^
    AttributeError: 'Book' object has no attribute '__Bprice'
'''

if __name__ == "__main__":
    main()

'''
OUTPUT
Book Name is:  Let's C
Book Author is:  ABC
Book Price is:  450.5
Let's C
ABC
'''