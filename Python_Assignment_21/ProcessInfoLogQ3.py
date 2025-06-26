import os
import sys
import time
import psutil
from FindRunningProcessQ2 import FindRunningProcess

def ProcessLog():
    DirectoryName = sys.argv[1]

        if not os.path.isdir(DirectoryName):
            os.makedirs(DirectoryName)

        timestamp = time.ctime()
        filename = "ProcessInfoLog%s.Log"%(timestamp)
        filename = filename.replace(" ","_")
        filename = filename.replace(":","_")

        fobj = open(filename , "w")
        process_info = FindRunningProcess()

        for pro in process_info:
            fobj.write(pro)

        fobj.close()

def main():
    try:
        if len(sys.argv) != 2:
            print("USAGE: ProcessInfoLogQ3.py <-DirectoryName->")
            return
        else:
            ProcessLog()

    except Exception as e:
        print("Exception Occured",e)
if __name__ == "__main__":
    main()