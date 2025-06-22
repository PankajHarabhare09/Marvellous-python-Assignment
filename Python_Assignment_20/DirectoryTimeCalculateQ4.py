import sys
import os
import time
from DirectoryRemovelQ3 import Duplicate_Removal

def main():
    try:
        timestamp = time.ctime()
        filename = "TimeCalculateLog%s.Log"%(timestamp)
        filename = filename.replace(" " , "_")
        filename = filename.replace(":" , "_")
        fobj.open(Filename , "w")

        start_time = time.time()
        Duplicate_Removal(sys.argv[1])
        end_time = time.time()

        Total_time_taken = end_time - start_time
        fobj.write("Total Time Taken for Deleting Duplicate files: ",Total_time_taken)

        fobj.close()
    except Exception as e:
        print("Exception Occured: ",e)

if __name__ == "__main__":
    main()