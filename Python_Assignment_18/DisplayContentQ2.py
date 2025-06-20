def main():

    FileName = input("Enter File Name That you Want To Open: ")

    Fobj = open(FileName , "r")

    print("-----> Content Of Given File <-----")
    Content = Fobj.read()
    print(Content)

    Fobj.close()
if __name__ == "__main__":
    main()

'''
OUTPUT

Enter File Name That you Want To Open: File5.txt
-----> Content Of Given File <-----
class Student:
    def __init__(self, A, B, C):
        self.Name = A           # public
        self._Age = B           # protected
        self.__Marks = C        # private

    def Display(self):
        print(self.Name)
        print(self._Age)
        print(self.__Marks)

obj = Student('Rahul',24,89)
obj.Display()

print(obj.Name)
print(obj._Age)
#print(obj.__Marks)
'''