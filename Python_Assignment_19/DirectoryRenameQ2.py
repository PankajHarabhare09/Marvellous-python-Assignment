import time
import sys
import os

def Rename_File(DirName , OldName , NewName):
    chkFile = os.path.isabs(DirName)
    if chkFile == False:
        chkFile = os.path.abspath(DirName)

    chkFile = os.path.exists(DirName)
    if chkFile == False:
        print("Path Invalid")
        return 
    
    chkFile = os.path.isdir(DirName)
    if chkFile == False:
        print("Path is Valid but Target is not Found")
        return

    timestamp = time.ctime()
    filename = "FileRenameLog%s.Log"%(timestamp)
    filename = filename.replace(" " , "_")
    filename = filename.replace(":" , "_")
    fobj = open(filename , "w")

    for FolderName , SubFolderNames , FileNames in os.walk(DirName):
        for files in FileNames:
            if files.endswith(OldName):
                old_path = os.path.join(FolderName , files)
                new_name = os.path.splitext(files)[0] + NewName
                new_path = os.path.join(FolderName , new_name)
                os.rename(old_path , new_path)
                fobj.write("Renamed Path: ",new_path)

    fobj.close()
def main():

    DirName = sys.argv[1]
    Old_Name = sys.argv[2]
    New_Name = sys.argv[3]

    try:
        if len(sys.argv) != 4:
            print("Usage: python DirectoryRenameQ2. py <-OldFileName-> <-NewFileName->")

        Rename_File(DirName , Old_Name , New_Name)

    except Exception as e:
        print("Exception Found: ",e)
if __name__ == "__main__":
    main()