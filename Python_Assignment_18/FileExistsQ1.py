import os
import sys

def main():
    FileName = input("Ente The File Name That you Want To Check: ")

    chkfile = os.path.isfile(FileName)

    if chkfile == True:
        print("File is  Present IN current Directory")
    else:
        print("File is Not Present in current Directory")

if __name__ == "__main__":
    main()