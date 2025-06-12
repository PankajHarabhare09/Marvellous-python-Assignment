import os

def main():
    print("Enter File Name That you have to Create: ")
    FileName = input()

    chkfile = os.path.exists(FileName)

    if chkfile == True:
        print("Give ",FileName," is already present in directory..!!")
    else:
        FObj = open(FileName , "w")
        print("Enter The Names Of Students: ")
        for i in range(5):
            StdName = input()
            FObj.writelines(StdName + "\n")
        FObj.close()

if __name__ == "__main__":
    main()