import os

def main():
    num = list()
    FileName = input("Enter The Name Of FIle That you want to Write: ")
    chkfile = os.path.exists(FileName)

    if chkfile == True:
        print("Given ",FileName," is Already Exists in Directory..!!")
    else:
        Fobj = open(FileName ,"w")
        print("Enter Data in That file: ")
        for i in range(1 , 11):
            data = input()
            Fobj.writelines(data + "\n")
        Fobj.close()

        Fobj2 = open(FileName , "r")
        print("File is Opend For Read: ")
        readdata = Fobj2.read()
        print("Data is: ",readdata)
        Fobj2.close()

if __name__ == "__main__":
    main()

'''
OUTPUT
Enter The Name Of FIle That you want to Write: Numbers.txt
Enter Data in That file:
1
2
3
4
5
6
7
8
9
10
File is Opend For Read:
Data is:  1
2
3
4
5
6
7
8
9
10
'''