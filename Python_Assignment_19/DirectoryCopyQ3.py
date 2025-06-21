import time
import sys
import os
import shutil

def Copy_File(SourceDir , DestDir):
    chkFile = os.path.isabs(SourceDir)
    if chkFile == False:
        chkFile = os.path.abspath(SourceDir)

    chkFile = os.path.exists(SourceDir)
    if chkFile == False:
        print("Path Invalid")
        return 
    
    chkFile = os.path.isdir(SourceDir)
    if chkFile == False:
        print("Path is Valid but Target is not Found")
        return

    timestamp = time.ctime()
    filename = "FileRenameLog%s.Log"%(timestamp)
    filename = filename.replace(" " , "_")
    filename = filename.replace(":" , "_")
    fobj = open(filename , "w")

    for FolderName , SubFolderNames , FileNames in os.walk(SourceDir):
        for files in FileNames:
            abs_path = os.path.join(FolderName , files)
            if os.path.isfile(abs_path):
                shutil.copy(SourceDir , DestDir)
                fobj.write("Copied: ",abs_path)
            
    fobj.close()
def main():
    try:
        if len(sys.argv) != 3:
            print("Usage: python DirectoryCopyQ3.py <-SourceDir-> <-DestinationDir->")

        SourceDir = sys.argv[1]
        DestDir = sys.argv[2]

        Copy_File(SourceDir , DestDir)

    except Exception as e:
        print("Exception Occured: ",e)

    
if __name__ == "__main__":
    main()