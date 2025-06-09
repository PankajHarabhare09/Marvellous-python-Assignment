import os

def main():
    print("Create 2 Files with Data For Comparision: ")
    File1 = input("1st File: ")
    File2 = input("2nd File: ")

    F1Obj = open(File1 , "w")
    F2Obj = open(File2 , "w")

    F1Data = input("Give Data for 1st File: ")
    F2Data = input("Give Data for 2nd File: ")

    F1 = F1Obj.write(F1Data)
    F2 = F2Obj.write(F2Data)

    if F1 == F2:
        print("Success")
    else:
        print("Failure")

    F1Obj.close()
    F2Obj.close()
    
if __name__ == "__main__":
    main()
'''
    OUTPUT
    Create 2 Files with Data For Comparision:
    1st File: File1.txt
    2nd File: File2.txt
    Give Data for 1st File: Jay Ganesh..!!!
    Give Data for 2nd File: Jay Ganesh..!!!
    Success
'''