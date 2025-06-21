import os
import sys
import time
import shutil

def Copy_File_With_Extension(SourceDir , DestDir , Ext):
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
            if file.endswith(Ext):
                src_path = os.path.join(FolderName , files)
                shutil.copy(src_path , DestDir)
                fobj.write("Copied: ",src_path)

    fobj.close()

def main():
    try:
        if len(sys.argv) != 4:
            print("Usage: DirectoryCopyExtensionQ4.py <SourceDir> <DestDir> <Extension>")
            return
        
        Source = sys.argv[1]
        Destination = sys.argv[2]
        Ext = sys.argv[3]

        Copy_File_With_Extension(Source , Destination , Ext)

    except Exception as e:
        print("Exception Occured: ",e)


if __name__ == "__main__":
    main()
