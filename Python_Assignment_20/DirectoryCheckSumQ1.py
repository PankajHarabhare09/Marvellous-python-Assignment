import os
import sys
import time
from FileUtilities import ChkDirectory , CalculateChecksum

def Display_Checksum(Dir):
    try:
        timestamp = time.ctime()
        filename = "ChecksumLog%s.Log"%(timestamp)
        filename = filename.replace(" " , "_")
        filename = filename.replace(":" , "_")

        fobj = open(filename , "w")
        ChkDirectory(Dir)
        for FolderName , SubFolderNames , FileNames in os.walk(Dir):
            for files in FileNames:
                abs_path = os.path.join(FolderName , files)
                chksum = CalculateChecksum(abs_path)
                fobj.write("CheckSum of Current file is: ",chksum)
        fobj.close()

    except Exception as e:
        print("Exception Occured: ",e)

def main():
    Border = "-"*54
    print(Border)
    print("--------------- Calculating Checksum ----------------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform directory cleaning")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory")
            print("Please provide valid absolute path")

        else:
            Display_Checksum(sys.argv[1])

    else:
        print("Invalid number of coomand line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage") 
    
    print(Border)
if __name__ == "__main__":
    main()