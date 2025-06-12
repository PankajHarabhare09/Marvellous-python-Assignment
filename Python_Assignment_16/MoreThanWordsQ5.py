import os

def main():
    word_count = 0
    print("Enter File Name That You want to Write And Read: ")
    FileName = input()

    chkfile = os.path.exists(FileName)

    if chkfile == True:
        print("Given ",FileName," is Already Exists in Directory..!")
    else:
        #WRITE THE FILE
        FobjW = open(FileName , "w")
        print("Enter Data in File: ")
        for i in range(5):
            WriteData = input()
            FobjW.writelines(WriteData + "\n")
        FobjW.close()

        #READ THE FILE
        print("File is opend for Read")
        Fobj = open(FileName , "r")
        readdata = Fobj.readlines()

        for data in readdata:
            word_count = word_count + len(data.split())

        if word_count >= 5:
            print(data)
        Fobj.close()

if __name__ == "__main__":
    main()

'''
    OUTPUT
    MoreThan5Words.txt
    Enter Data in File:
    Pankaj
    Kalash
    Ravi
    Hello How Are You Guys !
    I hope You Are Doing Well
    File is opend for Read
    I hope You Are Doing Well
'''