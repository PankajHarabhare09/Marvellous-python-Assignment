import os
def StudentInfo():
    Name = input("Enter Student Name: ")
    Marks = input("Enter Student Marks: ")
    return Name , Marks


def main():
    print("Enter The File Name That you Want to Write And Read: ")
    FileName = input()

    chkfile = os.path.exists(FileName)
    if chkfile == True:
        print("Given ",FileName," is Already Exists in Directory..!")
    else:
        FobjW = open(FileName , "w")
        print("Enter Student Name And Marks in File:")
        for i in range(5):
            data =  StudentInfo()
        
        FobjW.writelines(data)
        FobjW.close()

        FobjR = open(FileName , "r")
        print("-----File is Opend For Read-----")

        for line in FobjR:
            parts = line.strip().split()

            if len(parts) == 2:
                name , marks = parts

                if int(marks) > 75:
                    print(name,":", marks)

        FobjR.close()
if __name__ == "__main__":
    main()