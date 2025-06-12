import os

def main():
    print("Enter The File Name That You Want To Read: ")
    FileName = input()

    chkfile = os.path.exists(FileName)

    if chkfile == True:
        Fobj = open(FileName , "r")
        readData = Fobj.read()

        print("The ",FileName," Gives this Data: \n",readData)
    else:
        print("Give ",FileName," is not present in directory..!!")
        
if __name__ == "__main__":
    main()

'''
    OUTPUT
    Enter The File Name That You Want To Read:
    Student.txt
    The  Student.txt  Gives this Data:
    Pankaj
    john
    bob
    snow
    ella
'''