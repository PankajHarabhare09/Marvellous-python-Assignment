import sys
import os
import time
from datetime import datetime
from functionsInOneFile import DeleteDuplicates , SendMail

def main():
    try:
        if(len(sys.argv) == 4):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform Duplicate Files Removal")
            print("This is the directory automation script")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as ")
            print("ScriptName.py  NameOfDirctory TimeIntervalInMinutes EmailId")
            print("Please provide valid absolute path")

        else:
            NameOfDirctory = sys.argv[1]
            TimeIntervalInMinutes = int(sys.argv[2])
            EmailId = sys.argv[3]

            if not os.path.exists(NameOfDirctory) or not os.path.isdir(NameOfDirctory):
                print("Provide valid Name of Directory")
                return
            
            timestamp = time.ctime()
            filename ="MarvellousLog%s.Log"%(timestamp)
            filename = filename.replace(" " , "_")
            filename = filename.replace(":" , "_")

            fobj = open(filename , "w")

            DeleteDuplicate = DeleteDuplicates(NameOfDirctory)
            mailsend = (filename , EmailId , DeleteDuplicate)

            while True:
                time.sleep(TimeIntervalInMinutes * 60)
    else:
        print("Invalid number of coomand line arguments")
        print("Use the given flags as : ")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == "__main__":
    main()