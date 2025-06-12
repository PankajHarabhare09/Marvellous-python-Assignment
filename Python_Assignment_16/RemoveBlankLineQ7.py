import os

def main():
    space = 5
    print("Enter The File Name That You Want Write and Read: ")
    FileName = input()

    chkfile = os.path.exists(FileName)

    if chkfile == True:
        print("Given ",FileName," is Already Exists in Directory..!!")
    else:
        #WRITING THE FILE
        WFobj = open(FileName , "w")
        print("-----File Is Opend for Writing-----")
        print("Enter Data In your File: ")
        for i in range(5):
            Wdata = input()
            WFobj.writelines(Wdata + "\n")

        #READING THE FILE
        RFobj = open(FileName , "r")
        print("-----File is Opend For Reading-----")
        Rdata = RFobj.readlines()

        #Checking Blank lines
        for line in Rdata:
            if len(line.strip("\n")) >= space: #Strip is used for deleting white space (BY DEFAULT) or given character. 
                WFobj.write(line)
        print("Lines Deleted")

        WFobj.close()
        RFobj.close()

if __name__ == "__main__":
    main()

'''
OUTPUT
Enter The File Name That You Want Write and Read:
RemoveBlankLine.txt
-----File Is Opend for Writing-----
Enter Data In your File:

pankaj
hello

how are you
-----File is Opend For Reading-----
Lines Deleted
'''