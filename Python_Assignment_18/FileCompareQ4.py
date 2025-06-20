import sys
import os

def main():

    if len(sys.argv) != 3:
        print("USAGE: python FileCompareQ4.py File1.txt File2.txt")
        return

    File1 = sys.argv[1]
    File2 = sys.argv[2]

    F1obj = open(File1 , "r")
    F2obj = open(File2 , "r")

    Content1 = F1obj.read()
    Content2 = F2obj.read()

    if Content1 == Content2:
        print("Comparision Successfull")
    else:
        print("Comparision Failed")

if __name__ == "__main__":
    main()