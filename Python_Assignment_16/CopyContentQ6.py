import  os

def main():
    print("Write a File Name which You Want to Read Original Content: ")
    OGFile = input()

    ret = os.path.exists(OGFile)

    if ret == True:
        OGReadObj = open(OGFile , "r")

        print("Write a File Name which You Want to Copy that Original Content(ORIGINAL FILE): ")
        CopyFile = input()

        CopyObj = open(CopyFile , "a")
        CopyContent = CopyObj.write(OGReadObj.read())
        print("Copied Content From(",OGFile,") And Content is: ",CopyContent)

        OGReadObj.close()
        CopyObj.close()
    else:
        print("Given ",OGFile," is not Present in Directory..!!")

if __name__ == "__main__":
    main()

''' 
    OUTPUT
    Write a File Name which You Want to Read Original Content:
    Student.txt
    Write a File Name which You Want to Copy that Original Content(ORIGINAL FILE):
    StudentX.txt
    Copied Content From( Student.txt ) And Content is: Pankaj
    john
    bob
    snow
    ella
'''
